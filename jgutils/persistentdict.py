#!/usr/bin/env python3.7
"""Persistent Dictionary: Jerod Gawne, 2016.10.25 <https://github.com/jerodg/jgutils>"""
import csv
import json
import pickle
from copy import deepcopy
from logging import DEBUG, INFO, getLogger
from os import R_OK, access, chmod, fdopen, remove
from shutil import move
from sys import exc_info
from tempfile import mkstemp
from traceback import print_exception
from typing import NoReturn

logger = getLogger(__name__)
DBG = logger.isEnabledFor(DEBUG)
NFO = logger.isEnabledFor(INFO)


# todo: add HDF5 support
# todo: add zstd compression


class PersistentDict(dict):
    """Persistent, In-Memory dictionary
     - Auto-Discovery of input-file type
     - Output file-format: pickle, json, or csv"""

    def __init__(self, path: str, mode: str = 'c', access: int = None, fmt: str = 'pickle'):
        """
        :param path: str            
        :param mode: str; (r|c|n); r(eadonly), c(reate), n(ew)
        :param access: int; Octal
        :param fmt: str; (csv|json|pickle)"""
        super().__init__()
        self.PATH: str = path
        self.MODE: str = mode
        self.ACCESS: int = access
        self.FORMAT: str = fmt

        self.__load()

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sync()

    def __deepcopy__(self, requesteddeepcopy) -> object:
        """
        :param requesteddeepcopy:
        :return: PersistentDict()"""
        return deepcopy(self)

    def sync(self) -> NoReturn:
        """
        Save to temp file
        Overwrite persistence file with temp
        Set access permissions

        :return: NoReturn"""
        if self.MODE == 'r':
            if NFO:
                logger.info('Mode set as read-only; returning without committing to disk.')
            return

        # Reading an empty dictionary when using json or csv format causes an exception
        if (not self.items()) and (self.FORMAT != 'pickle'):
            if NFO:
                logger.info('Dictionary is empty; nothing to write')
            return

        fd, path = mkstemp(suffix=b'.tmp', text=False if self.FORMAT == 'pickle' else True)

        try:
            with fdopen(fd, 'wb+' if self.FORMAT == 'pickle' else 'w+') as fileobj:
                if self.FORMAT == 'csv':
                    csv.writer(fileobj).writerows(self.items())
                elif self.FORMAT == 'json':
                    json.dump(self, fileobj, separators=(',', ':'))
                elif self.FORMAT == 'pickle':
                    pickle.dump(obj=dict(self), file=fileobj, protocol=pickle.HIGHEST_PROTOCOL)
                else:
                    raise NotImplementedError(f'Unknown format: {self.FORMAT}')
        except OSError as ose:
            logger.exception(ose)
            remove(path)

        try:
            move(path, self.PATH)
        except OSError as ose:
            logger.exception(ose)

        if self.ACCESS:
            try:
                chmod(self.PATH, self.ACCESS)
            except OSError as ose:
                logger.exception(ose)

        if NFO:
            logger.info('Sync to disk complete.')

    def __load(self) -> NoReturn:
        """:return: NoReturn"""
        if self.MODE == 'n':
            if NFO:
                logger.info('File mode set to n(ew); not loading existing file.')
            return
        elif access(self.PATH, R_OK):
            with open(self.PATH, 'rb' if self.FORMAT == 'pickle' else 'r') as fileobj:
                for loader in (pickle.load, json.load, csv.reader):
                    fileobj.seek(0)
                    try:
                        return self.update(loader(fileobj))
                    except Exception as e:
                        logger.exception(e)
                        raise ValueError('File not in a supported format')
        if NFO:
            logger.info('Existing file sucessfully loaded.')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))

#!/usr/bin/env python3.7
# coding=utf-8
"""Persistent Dictionary: Jerod Gawne, 2016.10.25 <https://github.com/jerodg/jgutils>"""
import copy
import csv
import json
import logging
import os
import pickle
import shutil
import sys
import tempfile
import traceback
from typing import NoReturn

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class PersistentDict(dict):
    """Shelve-Persistent/In-Memory dictionary
     - Auto-Discovery of input-file type
     - Output file-format: pickle, json, or csv"""
    PATH: str
    MODE: str
    ACCESS: int
    FORMAT: str

    def __init__(self, path: str, mode: str = 'c', access: int = None, fmt: str = 'pickle'):
        """
        :param path: str            
        :param mode: str; 
            (r|c|n); r(eadonly), c(reate), n(ew)
        :param access: int; 
            Octal
        :param fmt: str; 
            (csv|json|pickle)"""
        super().__init__()
        self.PATH = path
        self.MODE = mode
        self.ACCESS = access
        self.FORMAT = fmt

        self.load()

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sync()

    def __deepcopy__(self, requesteddeepcopy) -> object:
        """
        :param requesteddeepcopy:
        :return: PersistentDict()"""
        return copy.deepcopy(self)

    def sync(self) -> NoReturn:
        """Sync to File

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

        fd, path = tempfile.mkstemp(suffix=b'.tmp', text=False if self.FORMAT == 'pickle' else True)

        try:
            with os.fdopen(fd, 'wb+' if self.FORMAT == 'pickle' else 'w+') as fileobj:
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
            os.remove(path)

        try:
            shutil.move(path, self.PATH)
        except OSError as ose:
            logger.exception(ose)

        if self.ACCESS is not None:
            try:
                os.chmod(self.PATH, self.ACCESS)
            except OSError as ose:
                logger.exception(ose)

        if NFO:
            logger.info('Sync to disk complete.')

    def load(self) -> NoReturn:
        """Load from disk

        :return: NoReturn"""
        if self.MODE == 'n':
            if NFO:
                logger.info('File mode set to n(ew); not loading existing file.')
            return

        if self.MODE != 'n' and os.access(self.PATH, os.R_OK):
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
        PATH = os.path.realpath('./test.pdb')
        with PersistentDict(path=PATH) as pd:
            pd['test'] = 123

        with PersistentDict(path=PATH) as pd:
            print('pd[test]: ', pd['test'])

        os.remove(PATH)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

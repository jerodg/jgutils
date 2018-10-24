#!/usr/bin/env python3.7
# coding=utf-8
"""Get files: Jerod Gawne, 2018.03.02 <https://github.com/jerodg>"""
import logging.config
import os
import sys
import traceback

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


def get_files(folder: str, extension: str='', prefix: str='', match: str='', sortedby='name', reverse=False) -> list:
    """Get Files

    :param folder: str; path to search
    :param extension: str; endswith match
    :param prefix: str; startswith match
    :param match: str; 'in' match (doesn't support wildcards)
    :param sortedby: str; (date|name|size)
    :param reverse: bool; sort reversed
    :return: list"""
    try:
        with os.scandir(folder) as inc_files:
            logger.info(f'Found {len(inc_files)} file(s).')
            files = [entry.path for entry in inc_files
                     if not entry.name.startswith('.') and entry.is_file()
                     and entry.name.endswith(extension) and entry.name.startswith(prefix)
                     and match in entry.name]

            logger.info(f'Found {len(files)} matching file(s).')

        if sortedby == 'name':
            return sorted(files, key=lambda x: x.name, reverse=reverse)
        elif sortedby == 'date':
            return sorted(files, key=lambda x: os.stat(x).st_mtime, reverse=reverse)
        elif sortedby == 'size':
            return sorted(files, key=lambda x: os.stat(x).st_size, reverse=reverse)
        else:
            logger.exception(f'Unknown sorted by parameter: {sortedby}')
            return files
    except OSError as ose:
        logger.exception(ose)
        return []


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

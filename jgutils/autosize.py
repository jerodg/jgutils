#!/usr/bin/env python3.7
"""Autosize: Jerod Gawne, 2018.01.15 <https://github.com/jerodg/jgutils>"""
import logging
from os import stat
from sys import exc_info
from traceback import print_exception
from typing import Union

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)

BP = {'B':   '',
      'KiB': 'Kibi',
      'MiB': 'Mebi',
      'GiB': 'Gibi',
      'TiB': 'Tebi',
      'PiB': 'Pebi',
      'EiB': 'Exbi',
      'ZiB': 'Zebi',
      'YiB': 'Yobi'}

DP = {'B':  '',
      'kB': 'Kilo',
      'MB': 'Mega',
      'GB': 'Giga',
      'TB': 'Tera',
      'PB': 'Peta',
      'EB': 'Exa',
      'ZB': 'Zetta',
      'YB': 'Yotta'}


# todo: allow to specify units


def autosize(path: Union[str, int] = None, size: int = None, prefix: str = 'binary', short: bool = True) -> str:
    """Autosize

    Works with file path or int

    :param path: str
    :param size: int
    :param prefix: string; binary|si
    :param short: bool
    :return: str"""
    try:
        numbytes = stat(path).st_size or size
    except FileNotFoundError as fnfe:
        logger.exception(fnfe)
        return f'File: {path} => Not Found'

    for key, value in BP.items() if prefix == 'binary' else DP.items():
        if abs(numbytes) < (1024.0 if prefix == 'binary' else 1000.0):
            return f'{numbytes:3.1f} {key if short else value}{"" if short else "-byte(s)"}'
        numbytes /= (1024.0 if prefix == 'binary' else 1000.0)


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))

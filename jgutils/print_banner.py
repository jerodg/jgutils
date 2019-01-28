#!/usr/bin/env python3.7
"""Print Banner: Jerod Gawne, 2018.08.17 <https://github.com/jerodg>"""
import logging
from sys import exc_info
from traceback import print_exception
from typing import NoReturn

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


def print_banner(message: str, width: int = 80, char: str = '*') -> NoReturn:
    msg_len = len(message)
    if msg_len >= width:
        print(message)

    ast = (width - msg_len) // 2
    ast = char * ast
    print(f'{ast}{message}{ast}\n')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))

#!/usr/bin/env python3.7
"""Easy Mail: Jerod Gawne, 2019.01.11 <https://github.com/jerodg>
Easy SMTP Emailer"""
import logging
from sys import argv, exc_info, exit
from traceback import print_exception

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


def main(*args: argv) -> int:
    """
    :param args:
    :return: int"""
    rc = 0

    return rc


if __name__ == '__main__':
    try:
        print(__doc__)
        exit(main(argv[1:]))
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))
        exit(1)

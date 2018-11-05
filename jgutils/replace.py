#!/usr/bin/env python3.7
# coding=utf-8
"""Replace: Jerod Gawne, 2018.11.05 <https://github.com/jerodg/jgutils>"""
import logging.config
import sys
import traceback

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


def replace(string: str, old: list, new: str, count: int = None) -> str:
    """Replace

    Based on the built-in replace.
    Accepts a list of 'old' substrings to be replaced by a single 'new' substring.

    https://docs.python.org/3.7/library/stdtypes.html#str.replace

    :param string: str
    :param old: list
    :param new: str
    :param count: int
    :return: str"""
    if type(old) is not list:
        old = list(old)

    for s in old:
        if count:
            string = string.replace(s, new, count)
        else:
            string = string.replace(s, new)

    return string


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

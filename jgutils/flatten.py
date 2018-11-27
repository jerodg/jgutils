#!/usr/bin/env python3.7
"""Flatten: Jerod Gawne, 2017.02.22 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from typing import Generator

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


def flatten(itr: (tuple, list)) -> Generator:
    """Reduce embedded lists/tuples into a single list (generator)

    :param itr: tuple|list
    :return: generator"""
    for item in itr:
        if isinstance(item, (tuple, list)):
            yield from flatten(item)
        else:
            yield item


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

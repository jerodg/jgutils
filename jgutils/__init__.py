#!/usr/bin/env python3.7
# coding=utf-8
"""jgutils Initialization: Jerod Gawne, 2018.10.19 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback

from jgutils import getfiles
from jgutils import persistentdict

___all___ = ['getfiles', 'naturalsort', 'persistentdict', 'replace', 'varprint']

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)

if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

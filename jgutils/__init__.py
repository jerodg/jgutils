#!/usr/bin/env python3.7
# coding=utf-8
"""jgutils Initialization: Jerod Gawne, 2018.10.19 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback

from jgutils import flatten
from jgutils import getfiles
from jgutils import naturalsort
from jgutils import persistentdict
from jgutils import replace
from jgutils import usholiday
from jgutils import varprint

___all___ = ['flatten', 'getfiles', 'naturalsort', 'persistentdict', 'replace', 'usholiday', 'varprint']

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)

if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

#!/usr/bin/env python3.7
# coding=utf-8
"""jgutils Initialization: Jerod Gawne, 2018.10.19 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback

from jgutils.tests import test_getfiles
from jgutils.tests import test_naturalsort
from jgutils.tests import test_persistentdict
from jgutils.tests import test_replace
from jgutils.tests import test_varprint

___all___ = ['test_getfiles', 'test_naturalsort', 'test_persistentdict', 'test_replace', 'test_varprint']

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)

if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

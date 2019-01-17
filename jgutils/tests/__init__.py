#!/usr/bin/env python3.7
"""jgutils Tests Initialization: Jerod Gawne, 2018.10.19 <https://github.com/jerodg/jgutils>"""
import logging
from sys import exc_info
from traceback import print_exception

from jgutils.tests import (test_dhms,
                           test_easymail,
                           test_flatten,
                           test_getfiles,
                           test_getips,
                           test_memsize,
                           test_naturalsort,
                           test_persistentdict,
                           test_replace,
                           test_request_debug,
                           test_usholiday,
                           test_varprint, )

___all___ = ['test_dhms',
             'test_easymail',
             'test_flatten',
             'test_getfiles',
             'test_getips',
             'test_memsize',
             'test_naturalsort',
             'test_persistentdict',
             'test_replace',
             'test_request_debug',
             'test_ushoiday',
             'test_varprint']

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)

if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))

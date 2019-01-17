#!/usr/bin/env python3.7
"""jgutils Initialization: Jerod Gawne, 2018.10.19 <https://github.com/jerodg/jgutils>"""
import logging
from sys import exc_info
from traceback import print_exception

from jgutils import (autosize,
                     dhms,
                     easymail,
                     flatten,
                     getfiles,
                     getips,
                     memsize,
                     naturalsort,
                     persistentdict,
                     replace,
                     request_debug,
                     usholiday,
                     varprint, )

___all___ = ['autosize',
             'dhms',
             'easymail',
             'flatten',
             'getfiles',
             'getips',
             'memsize',
             'naturalsort',
             'persistentdict',
             'replace',
             'requestdebug'
             'usholiday',
             'varprint']

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)

if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))

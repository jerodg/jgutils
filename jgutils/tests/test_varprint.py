#!/usr/bin/env python3.7
# coding=utf-8
"""Test Varprint: Jerod Gawne, 2018.11.06 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from unittest import TestCase

from jgutils import varprint

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestVarprint(TestCase):
    """TestVarprint"""

    def test_function(self):
        a = 'some_var'
        varprint.varprint(a)


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
#!/usr/bin/env python3.7
"""Test Varprint: Jerod Gawne, 2018.11.06 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from unittest import TestCase

from jgutils.print_banner import print_banner as printb
from jgutils.varprint import varprint as vp

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestVarprint(TestCase):
    """TestVarprint"""

    def test_function(self):
        printb('Basic Test')
        a = 'some_var'
        vp(a)
        print('')

    def test_object_without_length(self):
        printb('Test object without length')

        class A(object):
            def __init__(self):
                self.b = 0

        a = A()
        vp(a)
        print('')

    def test_list_unpacking(self):
        printb('Test list unpacking')
        a = ['one', 'two', 3, 'four']
        vp(a)
        print('')

    def test_dict_unpacking(self):
        printb('Test dict unpacking')
        a = {'one': 2, 'two': 3, 'three': 4}
        vp(a)
        print('')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

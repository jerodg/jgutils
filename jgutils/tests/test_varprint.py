#!/usr/bin/env python3.7
"""Test Varprint: Jerod Gawne, 2018.11.06 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from os.path import realpath

import pytest

from jgutils.persistentdict import PersistentDict as PerDi
from jgutils.print_banner import print_banner as printb
from jgutils.varprint import varprint as vp

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


@pytest.fixture(autouse=True)
def init_cache(request):
    pass


class TestVarprint(object):
    cache = PerDi(path=realpath('./data/test_varprint.cache'))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cache.sync()

    def test_function(self, request):
        a = 'some_var'
        vp(a)

        printb('Basic Test')

    def test_object_without_length(self, request):
        class A(object):
            def __init__(self):
                self.b = 0

        a = A()

        printb('Test object without length')
        vp(a)

    def test_list_unpacking(self, request):
        a = ['one', 'two', 3, 'four']

        printb('Test list unpacking')
        vp(a)

    def test_dict_unpacking(self, request):
        a = {'one': 2, 'two': 3, 'three': 4}

        printb('Test dict unpacking')
        vp(a)


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

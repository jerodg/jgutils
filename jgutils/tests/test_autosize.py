#!/usr/bin/env python3.7
"""Test Autosize: Jerod Gawne, 2019.01.15 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from os.path import realpath
from typing import NoReturn

import pytest

from jgutils.autosize import autosize
from jgutils.print_banner import print_banner as printb

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


@pytest.fixture(autouse=True)
def init_cache(request):
    pass


class TestAutosize(object):
    def test_return_type(self, request) -> NoReturn:
        file = realpath('./data/test_autosize.txt')
        size = autosize(file)

        assert size == '3.1 KiB'

        printb('Test Return Type')
        print(f'File: {file}\nSize: {size}')

    def test_file_not_found(self, request) -> NoReturn:
        file = realpath('./data/test_autosize2.txt')
        size = autosize(file)

        assert size == 'File Not Found'

        printb('Test File Not Found')
        print('file: ,', file)
        print(f'File: {file}\nSize: {size}')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

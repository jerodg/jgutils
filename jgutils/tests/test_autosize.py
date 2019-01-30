#!/usr/bin/env python3.7
"""Test Autosize: Jerod Gawne, 2019.01.15 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from os.path import realpath
from typing import NoReturn
from unittest import TestCase

from jgutils.autosize import autosize
from jgutils.print_banner import print_banner as printb

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestAutosize(TestCase):
    """Test Autosize"""

    def test_return_type(self) -> NoReturn:
        print('\n')
        printb('Test Return Type')
        file = realpath('./data/test_autosize.txt')
        size = autosize(file)
        print(f'File: {file}\nSize: {size}')
        self.assertTrue(size == '3.1 KiB')

    def test_file_not_found(self) -> NoReturn:
        print('\n')
        printb('Test File Not Found')
        file = realpath('./data/test_autosize2.txt')
        size = autosize(file)
        print(f'File: {file}\nSize: {size}')
        self.assertTrue(size == '3.1 KiB')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

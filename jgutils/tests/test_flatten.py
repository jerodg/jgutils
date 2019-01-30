#!/usr/bin/env python3.7
"""Test Flatten: Jerod Gawne, 2018.11.27 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from typing import Generator, NoReturn
from unittest import TestCase

from jgutils import flatten

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestFlatten(TestCase):
    """TestFlatten"""

    def test_return_type(self) -> NoReturn:
        """
        :return: NoReturn"""
        ls = flatten.flatten([1, 2, 3, [4, 5, 6, [7, 8, 9]]])
        self.assertTrue(isinstance(ls, Generator))

    def test_flattened(self) -> NoReturn:
        """Test if iterable is fully flattened

        :return: NoReturn"""
        ls = list(flatten.flatten([1, 2, 3, [4, 5, 6, [7, 8, 9]]]))
        for item in ls:
            self.assertNotIsInstance(item, (tuple, list))


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

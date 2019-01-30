#!/usr/bin/env python3.7
"""Test Requests Debug: Jerod Gawne, 2019.01.11 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from typing import Generator, NoReturn
from unittest import TestCase

from jgutils import flatten

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestRequestDebug(TestCase):
    """TestRequestDebug"""

    def test_return_type(self) -> NoReturn:
        """
        :return: NoReturn"""
        ls = flatten.flatten([1, 2, 3, [4, 5, 6, [7, 8, 9]]])
        # self.assertTrue(isinstance(ls, Generator))


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

#!/usr/bin/env python3.7
"""Test Memsize: Jerod Gawne, 2019.01.15 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from typing import Generator, NoReturn
from unittest import TestCase

from jgutils import flatten

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestMemsize(TestCase):
    """Test Memsize"""

    def test_return_type(self) -> NoReturn:
        """
        :return: NoReturn"""
        pass


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

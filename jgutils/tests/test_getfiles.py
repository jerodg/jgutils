#!/usr/bin/env python3.7
"""Test Getfiles: Jerod Gawne, 2018.11.05 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from os.path import realpath
from typing import NoReturn
from unittest import TestCase

from jgutils.getfiles import get_files

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


# todo: test recursion
# todo: test prefix
# todo: test suffix
# todo: test match
# todo: test sort
# todo: test main()/console script/entry point


class TestGetfiles(TestCase):
    def test_return_type(self) -> NoReturn:
        files = get_files(path=realpath('./'))
        self.assertTrue(isinstance(files, list))


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

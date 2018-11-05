#!/usr/bin/env python3.7
# coding=utf-8
"""Test Getfiles: Jerod Gawne, 2018.11.05 <https://github.com/jerodg/jgutils>"""
import logging
import os
import sys
import traceback
from unittest import TestCase

from jgutils import getfiles

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestGetfiles(TestCase):
    """TestReplace"""

    def test_return_type(self):
        files = getfiles.get_files(folder=os.path.realpath('./'))
        self.assertTrue(isinstance(files, list))


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

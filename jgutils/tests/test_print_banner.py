#!/usr/bin/env python3.7
"""Test Print Banner: Jerod Gawne, 2019.01.30 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from unittest import TestCase

from jgutils.print_banner import print_banner as pb

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestBannerPrint(TestCase):
    """Test Banner Print"""

    def test_return_type(self):
        print('\n')
        pb('Test Return Type')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

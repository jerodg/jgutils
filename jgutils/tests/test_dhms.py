#!/usr/bin/env python3.7
"""Test DHMS: Jerod Gawne, 2018.12.20 <https://github.com/jerodg/jgutils>"""
import logging
from datetime import timedelta
from sys import exc_info
from traceback import print_exception
from typing import NoReturn
from unittest import TestCase

from jgutils.dhms import dhms

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestDHMS(TestCase):
    def test_days(self) -> NoReturn:
        """
        :return: NoReturn"""
        td = timedelta(days=1)
        st = dhms(td)
        self.assertTrue(st == {'days': 1, 'hours': 0, 'minutes': 0, 'seconds': 0})


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))

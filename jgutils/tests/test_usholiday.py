#!/usr/bin/env python3.7
"""Test USHoliday: Jerod Gawne, 2018.11.21 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from datetime import date
from unittest import TestCase

from jgutils import usholiday

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestUsHoliday(TestCase):
    """TestUsHoliday"""

    def test_non_holiday(self):
        checkdate = date(year=2018, month=1, day=2)
        response = usholiday.usholiday(checkdate=checkdate)
        self.assertTrue(response is False)

    def test_holiday(self):
        checkdate = date(year=2018, month=1, day=1)
        response = usholiday.usholiday(checkdate=checkdate)
        self.assertTrue(response is True)

    def test_observed_holiday(self):
        checkdate = date(year=2018, month=11, day=12)
        response = usholiday.usholiday(checkdate=checkdate)
        self.assertTrue(response is True)


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

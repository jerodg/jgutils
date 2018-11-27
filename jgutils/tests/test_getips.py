#!/usr/bin/env python3.7
# coding=utf-8
"""Test Get IPs: Jerod Gawne, 2018.11.27 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from unittest import TestCase

from jgutils import getips

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestGetIps(TestCase):
    """TestGetIps"""

    def test_ips(self):
        with getips.GetIps() as gi:
            self.assertTrue(gi.ips['lan4'] is not None)


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

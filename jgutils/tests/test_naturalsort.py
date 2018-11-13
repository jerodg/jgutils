#!/usr/bin/env python3.7
# coding=utf-8
"""Test Natural Sort: Jerod Gawne, 2018.11.06 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from unittest import TestCase

from jgutils import naturalsort

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestNaturalSort(TestCase):
    """TestNaturalSort"""

    def test_list0(self):
        list0 = ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13', 'elm']
        test_list0 = ['elm', 'elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
        sorted_list0 = naturalsort.naturalsort(list0)
        self.assertTrue(sorted_list0 == test_list0)

    def test_list1(self):
        list1 = ['e0lm', 'e1lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm', 'e01lm']
        test_list1 = ['e0lm', 'e1lm', 'e01lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm']
        sorted_list1 = naturalsort.naturalsort(list1)
        self.assertTrue(sorted_list1 == test_list1)


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

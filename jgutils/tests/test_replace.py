#!/usr/bin/env python3.7
# coding=utf-8
"""Test Replace: Jerod Gawne, 2018.11.05 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback
from unittest import TestCase

from jgutils import replace

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestReplace(TestCase):
    """TestReplace"""

    def test_replace(self):
        string = 'CN=X545679,OU=Taco,DC=dmzedzedfive,DC=nachoburrito,DC=com'
        ls = ['CN=', 'OU=', 'DC=']
        replaced = replace.replace(string=string, old=ls, new='')
        self.assertTrue(replaced == 'X545679,Taco,dmzedzedfive,nachoburrito,com')

    def test_replace_with_count(self):
        string = 'CN=X545679,OU=Taco,DC=dmzedzedfive,DC=nachoburrito,DC=com'
        ls = ['CN=', 'OU=', 'DC=']
        replaced = replace.replace(string=string, old=ls, new='', count=1)
        self.assertTrue(replaced == 'X545679,Taco,dmzedzedfive,DC=nachoburrito,DC=com')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

#!/usr/bin/env python3.7
"""Test Persistent Dict: Jerod Gawne, 2018.10.19 <https://github.com/jerodg/jgutils>"""
import logging
import os
import sys
import traceback
from unittest import TestCase

from jgutils.persistentdict import PersistentDict as PD

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestPersistentDict(TestCase):
    """TestPersistentDict"""

    def test_is_dict(self):
        d = PD(path=os.path.realpath('./test_dict.pdb'))
        self.assertTrue(isinstance(d, dict))


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

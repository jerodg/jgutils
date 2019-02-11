#!/usr/bin/env python3.7
"""Test Easy Mail: Jerod Gawne, 2019.02.11 <https://github.com/jerodg/jgutils>"""
import logging
import os
import sys
import traceback
from typing import NoReturn

import pytest

from jgutils.persistentdict import PersistentDict as PD

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


# todo: write tests


@pytest.fixture(autouse=True)
def init_cache(request):
    pass


class TestEasyMail(object):
    cache = PD(path=os.path.realpath('./data/test_easymail.cache'))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cache.sync()

    def test_(self, request) -> NoReturn:
        pass


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

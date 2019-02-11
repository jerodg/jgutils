#!/usr/bin/env python3.7
"""Test Natural Sort: Jerod Gawne, 2018.11.06 <https://github.com/jerodg/jgutils>"""
import logging
import os
import random
import sys
import traceback
from typing import NoReturn

import pytest

from jgutils import naturalsort
from jgutils.persistentdict import PersistentDict as PD

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


@pytest.fixture(autouse=True)
def init_cache(request):
    pass


class TestNaturalSort(object):
    cache = PD(path=os.path.realpath('./data/test_naturalsort.cache'))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cache.sync()

    def test_numeric_at_beginning(self, request) -> NoReturn:
        unsorted = ['0elm', '1elm', '2Elm', '9elm', '10elm', '11Elm', '12Elm', '13elm', 'elm']
        random.shuffle(unsorted)
        test = ['0elm', '1elm', '2Elm', '9elm', '10elm', '11Elm', '12Elm', '13elm', 'elm']
        test_sorted = naturalsort.naturalsort(unsorted)

        assert test == test_sorted

    def test_numeric_at_end(self, request) -> NoReturn:
        unsorted = ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13', 'elm']
        random.shuffle(unsorted)
        test = ['elm', 'elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
        test_sorted = naturalsort.naturalsort(unsorted)

        assert test == test_sorted

    def test_numeric_intermixed(self, request) -> NoReturn:
        # todo: why do we get different results when shuffling the input?
        unsorted = ['e0lm', 'e1lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm', 'e01lm']
        random.shuffle(unsorted)
        test = ['e0lm', 'e1lm', 'e01lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm']
        test_sorted = naturalsort.naturalsort(unsorted)

        try:
            self.cache['test_numeric_intermixed'].add(tuple(test_sorted))
        except KeyError:
            self.cache['test_numeric_intermixed'] = set()
            self.cache['test_numeric_intermixed'].add(tuple(test_sorted))

        assert test == test_sorted

        if len(self.cache['test_numeric_intermixed']) > 1:
            if NFO:
                logger.info(f'Found {len(self.cache["test_numeric_intermixed"])} sorted variants')

    def test_numeric(self, request) -> NoReturn:
        unsorted = ['4.11.7402.0',
                    '4.7.7002.0',
                    '4.5.6806.0',
                    '4.9.7202.0',
                    '4.2.6402.0',
                    '4.14.7702.0',
                    '3.8.5907.0',
                    '3.7.5809.0',
                    '3.3.5410.0',
                    '4.10.7310.0', ]
        random.shuffle(unsorted)
        test = ['3.3.5410.0',
                '3.7.5809.0',
                '3.8.5907.0',
                '4.2.6402.0',
                '4.5.6806.0',
                '4.7.7002.0',
                '4.9.7202.0',
                '4.10.7310.0',
                '4.11.7402.0',
                '4.14.7702.0']
        test_sorted = naturalsort.naturalsort(unsorted)

        assert test == test_sorted

    # def test_integer(self, request) -> NoReturn:
    #     unsorted = [1, 2, 3, 11, 12, 13, 25, 27, 38]
    #     random.shuffle(unsorted)
    #     test = [1, 2, 3, 11, 12, 13, 25, 27, 38]
    #     test_sorted = naturalsort.naturalsort(unsorted)
    #
    #     assert test == test_sorted

    def test_last(self, request):
        for k, v in self.cache.items():
            print(k)
            for r in v:
                print(r)
        self.cache.sync()

    def test_dict_sort(self, request) -> NoReturn:
        pass

    def test_embedded_dict_sort(self, request) -> NoReturn:
        pass

    def test_mixed_list_dict_sort(self, request) -> NoReturn:
        pass

    def test_embedded_list_sort(self, request) -> NoReturn:
        pass


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

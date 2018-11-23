#!/usr/bin/env python3.7
"""Test Natural Sort: Jerod Gawne, 2018.11.06 <https://github.com/jerodg/jgutils>"""
import inspect
import logging
import sys
import traceback
from typing import NoReturn
from unittest import TestCase

import os
import random

from jgutils import naturalsort
from jgutils.persistentdict import PersistentDict as PD

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class TestNaturalSort(TestCase):
    """TestNaturalSort"""
    cache = PD(path=os.path.realpath('./test_naturalsort.cache'))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cache.sync()

    def test_numeric_at_beginning_mode1(self) -> NoReturn:
        """Tests sort when numerics are at the end

        :return: NoReturn"""
        unsorted = ['0elm', '1elm', '2Elm', '9elm', '10elm', '11Elm', '12Elm', '13elm', 'elm']
        random.shuffle(unsorted)
        test = ['0elm', '1elm', '2Elm', '9elm', '10elm', '11Elm', '12Elm', '13elm', 'elm']
        test_sorted = naturalsort.naturalsort(unsorted)

        s = str(inspect.currentframe().f_back.f_locals['self'])
        s = s[:s.index('(') - 1]
        try:
            self.cache[s].add(tuple(test_sorted))
        except KeyError:
            self.cache[s] = set()
            self.cache[s].add(tuple(test_sorted))

        try:
            self.assertTrue(test == test_sorted)
        except AssertionError as ae:
            logger.exception(ae)

        self.cache.sync()

    def test_numeric_at_beginning_mode2(self) -> NoReturn:
        """Tests sort when numerics are at the end

        :return: NoReturn"""
        unsorted = ['0elm', '1elm', '2Elm', '9elm', '10elm', '11Elm', '12Elm', '13elm', 'elm']
        random.shuffle(unsorted)
        test = ['elm', '0elm', '1elm', '2Elm', '9elm', '10elm', '11Elm', '12Elm', '13elm']
        test_sorted = naturalsort.naturalsort(unsorted, mode=2)

        s = str(inspect.currentframe().f_back.f_locals['self'])
        s = s[:s.index('(') - 1]
        try:
            self.cache[s].add(tuple(test_sorted))
        except KeyError:
            self.cache[s] = set()
            self.cache[s].add(tuple(test_sorted))

        try:
            self.assertTrue(test == test_sorted)
        except AssertionError as ae:
            logger.exception(ae)

        self.cache.sync()

    def test_numeric_at_end_mode1(self) -> NoReturn:
        """Tests sort when numerics are at the end

        :return: NoReturn"""
        unsorted = ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13', 'elm']
        random.shuffle(unsorted)
        test = ['elm', 'elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
        test_sorted = naturalsort.naturalsort(unsorted)

        s = str(inspect.currentframe().f_back.f_locals['self'])
        s = s[:s.index('(') - 1]
        try:
            self.cache[s].add(tuple(test_sorted))
        except KeyError:
            self.cache[s] = set()
            self.cache[s].add(tuple(test_sorted))

        try:
            self.assertTrue(test == test_sorted)
        except AssertionError as ae:
            logger.exception(ae)

        self.cache.sync()

    def test_numeric_at_end_mode2(self) -> NoReturn:
        """Tests sort when numerics are at the end

        :return: NoReturn"""
        unsorted = ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13', 'elm']
        random.shuffle(unsorted)
        test = ['elm', 'elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
        test_sorted = naturalsort.naturalsort(unsorted, mode=2)

        s = str(inspect.currentframe().f_back.f_locals['self'])
        s = s[:s.index('(') - 1]
        try:
            self.cache[s].add(tuple(test_sorted))
        except KeyError:
            self.cache[s] = set()
            self.cache[s].add(tuple(test_sorted))

        try:
            self.assertTrue(test == test_sorted)
        except AssertionError as ae:
            logger.exception(ae)

        self.cache.sync()

    def test_numeric_intermixed_mode1(self) -> NoReturn:
        """Tests sort when numerics are in the middle

        :return: NoReturn"""
        # todo: why do we get different results when shuffling the input?
        unsorted = ['e0lm', 'e1lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm', 'e01lm']
        random.shuffle(unsorted)
        test = ['e0lm', 'e1lm', 'e01lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm']
        test_sorted = naturalsort.naturalsort(unsorted)

        s = str(inspect.currentframe().f_back.f_locals['self'])
        s = s[:s.index('(') - 1]
        try:
            self.cache[s].add(tuple(test_sorted))
        except KeyError:
            self.cache[s] = set()
            self.cache[s].add(tuple(test_sorted))

        try:
            self.assertTrue(test == test_sorted)
        except AssertionError as ae:
            logger.exception(ae)

        if len(self.cache[s]) > 1:
            if NFO:
                logger.info(f'Found {len(self.cache[s])} sorted variants')

        self.cache.sync()

    def test_numeric_intermixed_mode2(self) -> NoReturn:
        """Tests sort when numerics are in the middle

        :return: NoReturn"""
        # todo: why do we get different results when shuffling the input?
        unsorted = ['e0lm', 'e1lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm', 'e01lm']
        random.shuffle(unsorted)
        test = ['elm', 'e0lm', 'e1lm', 'E2lm', 'e9lm', 'e01lm', 'e10lm', 'E12lm', 'e13lm']
        test_sorted = naturalsort.naturalsort(unsorted, mode=2)

        s = str(inspect.currentframe().f_back.f_locals['self'])
        s = s[:s.index('(') - 1]
        try:
            self.cache[s].add(tuple(test_sorted))
        except KeyError:
            self.cache[s] = set()
            self.cache[s].add(tuple(test_sorted))

        try:
            self.assertTrue(test == test_sorted)
        except AssertionError as ae:
            logger.exception(ae)

        self.cache.sync()

    def test_numeric_mode1(self) -> NoReturn:
        """ Tests sort when numerics + punctuation only

        :return: NoReturn"""
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

        s = str(inspect.currentframe().f_back.f_locals['self'])
        s = s[:s.index('(') - 1]
        try:
            self.cache[s].add(tuple(test_sorted))
        except KeyError:
            self.cache[s] = set()
            self.cache[s].add(tuple(test_sorted))

        try:
            self.assertTrue(test == test_sorted)
        except AssertionError as ae:
            logger.exception(ae)

        self.cache.sync()

    def test_numeric_mode2(self) -> NoReturn:
        """ Tests sort when numerics + punctuation only

        :return: NoReturn"""
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
        test_sorted = naturalsort.naturalsort(unsorted, mode=2)

        s = str(inspect.currentframe().f_back.f_locals['self'])
        s = s[:s.index('(') - 1]
        try:
            self.cache[s].add(tuple(test_sorted))
        except KeyError:
            self.cache[s] = set()
            self.cache[s].add(tuple(test_sorted))

        try:
            self.assertTrue(test == test_sorted)
        except AssertionError as ae:
            logger.exception(ae)

        self.cache.sync()

    def test_integer(self) -> NoReturn:
        """Tests sort when only integers

        :return: NoReturn"""
        unsorted = [1, 2, 3, 11, 12, 13, 25, 27, 38]
        random.shuffle(unsorted)
        test = [1, 2, 3, 11, 12, 13, 25, 27, 38]
        test_sorted = naturalsort.naturalsort(unsorted)

        s = str(inspect.currentframe().f_back.f_locals['self'])
        s = s[:s.index('(') - 1]
        try:
            self.cache[s].add(tuple(test_sorted))
        except KeyError:
            self.cache[s] = set()
            self.cache[s].add(tuple(test_sorted))

        try:
            self.assertTrue(test == test_sorted)
        except AssertionError as ae:
            logger.exception(ae)

        self.cache.sync()

    def test_last(self):
        for k, v in self.cache.items():
            print(k)
            for r in v:
                print(r)
        self.cache.sync()


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

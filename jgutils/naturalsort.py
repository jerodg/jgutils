#!/usr/bin/env python3.7
# coding=utf-8
"""Natural-Sort: Jerod Gawne, 2016.05.04 <https://github.com/jerodg/jgutils>"""

import logging
import re
import sys
import traceback

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)
DRE = re.compile(r'(\d+)')


def naturalsort(ls, mode=1) -> list:
    """Natural-Sort

    Sorting for Humans; Two Modes

    mylist = ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13', 'elm']
    mode1 =  ['elm', 'elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
    mode2 =  ['elm', 'elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']

    mylist1 = ['e0lm', 'e1lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm', 'e01lm']
    mode1 =   ['e0lm', 'e1lm', 'e01lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm']
    mode2 =   ['elm', 'e0lm', 'e1lm', 'E2lm', 'e9lm', 'e01lm', 'e10lm', 'E12lm', 'e13lm']

    :param ls: list
    :param mode: int (1|2)
    :return: list"""

    if mode == 1:
        return sorted(ls, key=lambda _: [int(s) if s.isdigit() else s.lower() for s in re.split(DRE, _)])
    elif mode == 2:
        fmt = ['{', '0', ':', '>', str(len(max(ls, key=len))), '}']
        return sorted(ls, key=lambda _: ''.join(fmt).format(_, max(ls, key=len)).lower())
    else:
        raise NotImplementedError


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

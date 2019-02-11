#!/usr/bin/env python3.7
"""Natural-Sort: Jerod Gawne, 2016.05.04 <https://github.com/jerodg/jgutils>"""
import logging
import re
import sys
import traceback
from typing import Union

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)
DRE = re.compile(r'(\d+)')


def naturalsort(item: Union[list, dict], sort_order: str = 'ASC') -> Union[list, dict]:
    """Sorting for Humans"""

    # todo: open these loops up and add cross-call for multiple embedded types (list, dict, tuple)
    def sort_dict(item: dict, rvrs: bool):
        return {k: sort_dict(v, rvrs=rvrs) if isinstance(v, dict) else v for k, v in
                sorted(item.items(), key=lambda _: [int(s) if s.isdigit() else s.lower() for s in re.split(DRE, _)],
                       reverse=rvrs)}

    def sort_list(item: list, rvrs: bool):
        return [sort_list(x, rvrs=rvrs) if isinstance(x, list) else x for x in
                sorted(item, key=lambda _: [int(s) if s.isdigit() else s.lower() for s in re.split(DRE, _)],
                       reverse=rvrs)]

    rvrs = True if sort_order == 'DESC' else False

    if type(item) is list:
        return sort_list(item, rvrs)
    elif type(item) is dict:
        return sort_dict(item, rvrs)
    else:
        raise NotImplementedError


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

#!/usr/bin/env python3.7
"""Memsize: Jerod Gawne, 2018.01.15 <https://github.com/jerodg/jgutils>"""
import logging
from inspect import isgetsetdescriptor, ismemberdescriptor
from sys import exc_info, getsizeof
from traceback import print_exception
from typing import Any, Union

from jgutils.autosize import autosize

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


def memsize(obj: Any, seen: set = None, human: bool = False) -> Union[int, str]:
    """Calculate size of object in bytes

    :param obj: Any
    :param seen: set
    :param human: bool
    :return: int"""
    size = getsizeof(obj)
    seen = seen or set()
    obj_id = id(obj)

    if obj_id in seen:
        return 0

    seen.add(obj_id)

    if hasattr(obj, '__dict__'):
        for cls in obj.__class__.__mro__:
            if '__dict__' in cls.__dict__:
                d = cls.__dict__['__dict__']
                if isgetsetdescriptor(d) or ismemberdescriptor(d):
                    size += memsize(obj.__dict__, seen)
                break

    if isinstance(obj, dict):
        size += sum((memsize(v, seen) for v in obj.values()))
        size += sum((memsize(k, seen) for k in obj.keys()))
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum((memsize(i, seen) for i in obj))

    if hasattr(obj, '__slots__'):  # can have __slots__ with __dict__
        size += sum(memsize(getattr(obj, s), seen) for s in obj.__slots__ if hasattr(obj, s))

    if human:
        return autosize(size=size)

    return size


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))

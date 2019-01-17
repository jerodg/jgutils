#!/usr/bin/env python3.7
"""Days Hours Minutes Seconds: Jerod Gawne, 2018.12.20 <https://github.com/jerodg/jgutils>"""
import logging.config
from datetime import timedelta
from sys import exc_info
from traceback import print_exception

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


def dhms(td: timedelta) -> dict:
    """Days, Hours, Minutes, Seconds

    :param td: datetime.timedelta
    :return: dict"""
    h = td.seconds // 3600
    m = (td.seconds - h * 3600) // 60
    s = td.seconds - (h * 3600) - (m * 60)
    return {'days': td.days, 'hours': h, 'minutes': m, 'seconds': s}


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))

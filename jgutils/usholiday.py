#!/usr/bin/env python3.7
"""US Holiday: Jerod Gawne, 2017.08.25 <https://github.com/jerodg/jgutils>
New years: January 1
Martin Luther King Jr.: 3rd Monday in January
Washington's Birthday (Presidents): 3rd Monday in February
Memorial: Last Monday in May
Independance: July 4
Labor: First Monday in September
Columbus: Second Monday in October
Veterans: November 11
Thanksgiving: Fourth Thursday in November
"""
import logging
import sys
from calendar import monthcalendar
from datetime import date
from datetime import datetime
from datetime import timedelta

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


def usholiday(checkdate=None) -> bool:
    """Is date or today a US Federal Holiday?
    
    :param checkdate: (datetime.date|datetime.datetime|str<YYYYmmdd>)
    :return: bool"""
    if type(checkdate) is datetime:
        checkdate = datetime.date(checkdate)
    elif type(checkdate) is str:
        # todo: auto determine date format
        checkdate = datetime.strptime(checkdate, '%Y%m%d')
    elif type(checkdate) is date:
        pass
    elif checkdate is None:
        checkdate = date.today()
    else:
        raise NotImplementedError

    tdy: date = checkdate
    memorial: monthcalendar = monthcalendar(tdy.year, 5)
    labor: monthcalendar = monthcalendar(tdy.year, 9)
    thanksgiving: monthcalendar = monthcalendar(tdy.year, 11)
    dplus = timedelta(days=1)
    dminus = timedelta(days=-1)

    holidays = ['0101',  # New tdy.years
                f'01{monthcalendar(tdy.year, 1)[3][0]:0>2}',  # Martin Luther King Jr.
                f'02{monthcalendar(tdy.year, 2)[3][0]:0>2}',  # Washington's Birthday (Presidents)
                f'05{memorial[-1][0] if memorial[-1][0] > 0 else memorial[-2][0]:0>2}',  # Memorial
                '0704',  # Independance
                f'09{labor[0][0] if labor[0][0] > 0 else labor[1][0]:0>2}',  # Labor
                f'09{monthcalendar(tdy.year, 10)[2][0]:0>2}',  # Columbus Day
                '1111',  # Veterans
                f'11{thanksgiving[3][3]:0>2}',  # Thanksgiving
                '1225'  # Christmas
                ]

    # Monday is 0 and Sunday is 6
    holidays = [datetime.strptime(f'{d}{tdy.year}', '%m%d%Y') for d in holidays]
    dayofweek = [d.weekday() for d in holidays]

    for i, day in enumerate(dayofweek):
        if day == 5:
            h = holidays[i] + dminus
        elif day == 6:
            h = holidays[i] + dplus
        else:
            h = None
        if h:
            holidays.append(h)

    holidays = [datetime.date(d) for d in holidays]

    return True if tdy in holidays else False


if __name__ == '__main__':
    try:
        # print(__doc__)
        print(usholiday())
    except Exception as excp:
        import traceback

        logger.exception(traceback.print_exception(*sys.exc_info()))

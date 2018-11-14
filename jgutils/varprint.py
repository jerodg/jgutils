#!/usr/bin/env python3.7
# coding=utf-8
"""Variable Printer: Jerod Gawne, 2018.02.27 <https://github.com/jerodg/jgutils>"""
import inspect
import logging.config
import sys
import traceback
from typing import NoReturn

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


def varprint(var) -> NoReturn:
    """Variable Printer

    Prints the name of the variable and the value.

    [<variable_name>] (<variable_length>): <variable_content>

    :param var: object
    :return: NoReturn"""
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()

    for var_name, var_val in callers_local_vars:
        if var_val is var:
            try:
                print(f'[{var_name}]<{type(var)}>({len(var)}): {var}')
            except TypeError as te:
                logger.warning(te)
                print(f'[{var_name}]<{type(var)}>({len(var)}): {var}')
            return


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

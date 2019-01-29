#!/usr/bin/env python3.7
"""Variable Printer: Jerod Gawne, 2018.02.27 <https://github.com/jerodg/jgutils>"""
import inspect
import logging.config
import sys
import traceback
from typing import NoReturn

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


# todo: handle classes
# todo: handle generic objects


def varprint(var) -> NoReturn:
    """Variable Printer

    Prints the name of the variable and the value.

    [<variable_name>] (<variable_length>): <variable_content>

    Not all objects support length

    :param var: object
    :return: NoReturn"""
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()

    for var_name, var_val in callers_local_vars:
        if var_val is var:
            t = type(var)
            typ = str(t)
            typ = typ[typ.index("'") + 1:-2]

            try:
                length = len(var)
            except TypeError:
                length = 'N/A'

            if t is list:
                print(f'{var_name}: {typ} = ({length}):')
                [print(f'\t{i}') for i in var]
            elif t is dict:
                print(f'{var_name}: {typ} = ({length}):')
                [print(f'\t{k}: {v}') for k, v in var.items()]
            else:
                print(f'{var_name}: {typ} = ({length}) {var}')


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

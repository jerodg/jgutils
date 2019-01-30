#!/usr/bin/env python3.7
"""Get Files: Jerod Gawne, 2018.03.02 <https://github.com/jerodg/jgutils>"""
import argparse
import logging
from os import getcwd, scandir, stat
from sys import exc_info
from traceback import print_exception
from typing import Generator

from jgutils.naturalsort import naturalsort as ns

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


# todo: wildcard matching


def get_files(path: str, recursive=False, prefix: str = '', suffix: str = '', match: str = '',
              sortby: str = 'name', sort_order: str = 'ASC') -> list:
    """
    :param path: str; path to search
    :param recursive: bool; search folders beneath root path
    :param prefix: str; startswith match
    :param suffix: str; endswith match

    :param match: str; basic 'in' match (doesn't support wildcards)
    :param sortby: str; (name|natural|date|size)
    :param sort_order: str; (ASC|DSC)

    :return: list"""

    def scantree(path) -> Generator:
        """Recursively yield DirEntry objects for given directory"""
        with scandir(path) as st:
            for entry in st:
                if entry.is_dir(follow_symlinks=False):
                    yield from scantree(entry.path)
                else:
                    yield entry

    rvrs = True if sort_order == 'DESC' else False

    try:
        if recursive:
            entries = scantree(path)
        else:
            entries = scandir(path)

        files = [entry.path for entry in entries
                 if not entry.name.startswith('.')
                 and entry.is_file()
                 and entry.name.endswith(suffix)
                 and entry.name.startswith(prefix)
                 and match in entry.name]
        if DBG:
            logger.info(f'Found {len(files)} matching file(s).')

        if sortby == 'name':
            return sorted(files, reverse=rvrs)
        elif sortby == 'natural':
            return ns(files, sort_order='DESC' if rvrs else 'ASC')
        elif sortby == 'date':
            return sorted(files, key=lambda x: stat(x).st_mtime, reverse=rvrs)
        elif sortby == 'size':
            return sorted(files, key=lambda x: stat(x).st_size, reverse=rvrs)
        else:
            logger.exception(f'Unknown sorted by parameter: {sortby}')
            return files

    except OSError as ose:
        logger.exception(ose)
        return []


def main():
    """Entry Point for Console Script"""
    parser = argparse.ArgumentParser(description='Get a list of files..')
    parser.add_argument('path', metavar='p', type=str, default=getcwd(), help='path to folder')
    parser.add_argument('-recursive', metavar='-r', type=bool, help='search recursively')
    parser.add_argument('-prefix', metavar='-p', type=str, help='file prefix')
    parser.add_argument('-suffix', metavar='-s', type=str, help='file suffix (extension)')
    parser.add_argument('-match', metavar='-m', type=str, help='"in" match')
    parser.add_argument('-sortby', metavar='-sb', type=str, choices=['name', 'natural', 'date', 'size'],
                        help='sort by...')
    parser.add_argument('-sort_order', metavar='-so', type=str, choices=['ASC', 'DSC'], help='sort order')

    args = parser.parse_args()

    files = get_files(path=args.path, recursive=args.recursive, prefix=args.prefix, suffix=args.suffix,
                      match=args.match,
                      sortby=args.sortby, sort_order=args.sort_order)

    print(*files, sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))

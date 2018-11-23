#!/usr/bin/env python3.7
# coding=utf-8
"""jgutils Setup: Jerod Gawne, 2018.10.19 <https://github.com/jerodg/jgutils>"""
import logging
import sys
import traceback

import setuptools

logger = logging.getLogger(__name__)
name = 'jgutils'


def readme() -> str:
    """Readme

    :return: str"""
    with open('README.md') as f:
        return f.read()


if __name__ == '__main__':
    try:
        setuptools.setup(name='jgutils',
                         version='0.6.2.5',
                         description='jerodg.com utilities module',
                         long_description=readme(),
                         long_description_content_type='text/markdown',
                         classifiers=[
                             'Development Status :: 3 - Alpha',
                             'Environment :: Console',
                             'Intended Audience :: End Users/Desktop',
                             'Intended Audience :: Developers',
                             'Intended Audience :: System Administrators',
                             'License :: OSI Approved :: GNU Affero General Public License v3',
                             'Natural Language :: English',
                             'Operating System :: MacOS :: MacOS X',
                             'Operating System :: Microsoft :: Windows',
                             'Operating System :: POSIX',
                             'Programming Language :: Python',
                             'Topic :: Utilities'],
                         keywords='utility utilities persistent dictionary file list listing',
                         url='http://github.com/jerodg/jgutils',
                         author='Jerod Gawne',
                         author_email='jerodgawne@gmail.com',
                         license='AGPLv3',
                         packages=setuptools.find_packages(),
                         install_requires=[],
                         include_package_data=True,
                         zip_safe=False,
                         test_suite='nose.collector',
                         tests_require=['nose'],
                         scripts=[],
                         entry_points={'console_scripts': []})
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))

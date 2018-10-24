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
    with open('README.adoc') as f:
        return f.read()


if __name__ == '__main__':
    try:
        setuptools.setup(name='jgutils',
                         version='0.2.0',
                         description='jerodg.com utilities module',
                         long_description=readme(),
                         long_description_content_type='text/asciidoctor',
                         classifiers=['Development Status :: 3 - Alpha',
                                      'License :: OSI Approved :: MIT License',
                                      'Programming Language :: Python :: 3.7',
                                      'Environment :: Console',
                                      'Intended Audience:: Developers',
                                      'Natural Language :: English',
                                      'Operating System :: Microsoft :: Windows :: Windows 10 :: Windows 8 :: Windows '
                                      '7 :: POSIX :: iOS',
                                      'Topic :: Utilities'],
                         keywords='utility utilities persistent dictionary file list listing',
                         url='http://github.com/jerodg/jgutils',
                         author='Jerod Gawne',
                         author_email='jerodgawne@gmail.com',
                         license='MIT',
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

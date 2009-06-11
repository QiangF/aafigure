# $Id$
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Author: Chris Liechti <cliechti@gmx.net>
# Copyright: This file has been placed in the public domain.

from distutils.core import setup

setup(
    name = 'aafigure',
    version = '0.2',
    description = "ASCII art to image converter",
    url = 'http://launchpad.net/aafigure',
    license = 'BSD',
    long_description = """\
This package provides a module ``aafigure``, that can be used from other
programs, and a command line tool ``aafigure``.

Example, test.txt::

            +-----+   ^
            |     |   |
        --->+     +---o--->
            |     |   |
            +-----+   V

Command::

    aafigure test.txt -t svg -o test.svg

Please see README.txt for examples.
""",
    author = 'Chris Liechti',
    author_email = 'cliechti@gmx.net',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms = 'any',
    packages = ['aafigure'],
    scripts = ['scripts/aafigure'],
)

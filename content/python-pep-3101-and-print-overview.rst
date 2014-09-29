========================================
Python PEP 3101 and ``print()`` Overview
========================================

:date: 2014-09-29T13:14-0600
:author: carlos-jenkins
:category: programming
:tags: python, pep3101
:slug: python-pep-3101-and-print-overview

Python `PEP 3101`_ specifies the `string formatting function`_ that replaces
the old ``%`` operator on strings. In addition, `PEP 3105`_ also specifies the
behavior of the ``print()``, now standard in Python 3. This post shows a small
cheat-sheet or overview of both.

.. _PEP 3101: http://legacy.python.org/dev/peps/pep-3101/
.. _string formatting function: https://docs.python.org/3.4/library/string.html#string.Formatter.format
.. _PEP 3105: http://legacy.python.org/dev/peps/pep-3105/


.. code:: pycon

   # Overview of PEP 3101 and PEP 3105
   # In Python 2.7 use with:
   from __future__ import print_function

   # Print to stderr
   >>> from sys import stderr
   >>> print('ABC', file=stderr)
   ABC

   # Print without a newline
   >>> print('ABC', end='')
   ABC>>>

   # Print multiple elements
   >>> print('A', 'B', 'C', sep=', ')
   A, B, C

   # Print in hexadecimal
   >>> print('0x{:X}'.format(15))
   0xF

   # Print in octal
   >>> print('0{:o}'.format(15))
   017

   # Print in binary
   >>> print('b{:b}'.format(15))
   b1111
   >>> print('b{:08b}'.format(15))
   b00001111

   # Print with leading zeros
   >>> print('{:04d}'.format(15))
   0015

   # Print float with fixed precision
   >>> print('{:.2f}'.format(15.0))
   15.00

   # Print with leading or trailing characters
   >>> print('{:_>12}'.format('My String'))
   ___My String
   >>> print('{:_<12}'.format('My String'))
   My String___

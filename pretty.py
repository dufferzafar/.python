"""
Helper functions to pretty print datastructures.

Supports:

    Dictionaries (JSON)
"""

from __future__ import print_function

# ANSI color terminal escape sequences
KEY_COLOR = '[32m'
VAL_COLOR = '[33m'


def json(inp, indent=''):
    """ Print a colored JSON. """

    print('{')

    for key, val in inp.items():

        print('{}  {}"{}"{} : '.format(indent, KEY_COLOR, key, VAL_COLOR), end='')

        if isinstance(val, dict):
            json(val, indent + '  ')
        elif isinstance(val, str):
            print('"{}",'.format(val))
        else:
            print('{},'.format(val))

    print('[0m' + indent + '}')

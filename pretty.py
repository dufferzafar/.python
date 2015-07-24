"""
Helper functions to pretty print datastructures.

Supports:

    Dictionaries (JSON)
"""


def json(keyvals, indent=''):
    """ Print a colored JSON. """
    # ANSI color terminal escape sequences
    KEY_COLOR = '[32m'
    VAL_COLOR = '[33m'

    print '{'

    for key, val in keyvals.iteritems():

        print '{}  {}"{}"{}:'.format(indent, KEY_COLOR, key, VAL_COLOR),
        if isinstance(val, dict):
            pretty_print(val, indent + '  ')
        elif isinstance(val, str):
            print '"{}",'.format(val)
        else:
            print '{},'.format(val)

    print '[0m' + indent + '}'

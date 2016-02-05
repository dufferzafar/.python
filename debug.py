"""
Functions to help me debug.

Originally created to debug mitmproxy objects:
>>> import debug
>>> debug.dump_attrs(flow.request, "/tmp/mitmproxy-debug.json", "a")

Could be replaced by:
https://github.com/zestyping/q
"""

from __future__ import print_function


def dump_attrs(obj, file, mode):
    """ Dump all attributes of an object to a json file."""

    import json

    attrs = {}
    for attr in dir(obj):

        # Skip private attributes
        if attr.startswith("_"):
            continue

        try:
            val = getattr(obj, attr)

            # Skip functions
            if callable(val):
                continue
        except:
            pass
        else:
            attrs[attr] = str(val)

    with open(file, mode) as out:
        json.dump(attrs, out, sort_keys=True, indent=2)

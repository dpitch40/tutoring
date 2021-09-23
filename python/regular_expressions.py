import re
from collections import OrderedDict
import pprint

def _multi(f, pattern, strings, *args, **kwargs):
    matches = OrderedDict()
    for s in strings:
        m = f(pattern, s, *args, **kwargs)
        if m:
            matches[s] = m.groups()
    pprint.pprint(matches, sort_dicts=False)

def multisearch(pattern, strings, *args, **kwargs):
    return _multi(re.search, pattern, strings, *args, **kwargs)

def multimatch(pattern, strings, *args, **kwargs):
    return _multi(re.match, pattern, strings, *args, **kwargs)

# -*- coding: utf-8 -*-
# flake8: noqa
"""
CommandLine:
    # Partially regenerate __init__.py
    python -c "import ubelt"
    python -c "import ubelt" --print-ubelt-init
    python -c "import ubelt" --update-ubelt-init --dyn

TODO:
    The following functions and classes are candidates to be ported from utool:
    * reload_class
    * inject_func_as_method
    * inject_func_as_property
    * embed
    * repr2
    * identity
    * rsync
    * grab_file_url
    * parse_cfgstr3
    * accumulate
    * itertwo
    * iterwin
    * ParamInfo - move to dtool
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import sys

__version__ = '0.0.23'

GLOBAL_MODULES = [
    'util_const',
    'util_decor',
    'util_dict',
    'util_cache',
    'util_io',
    'util_list',
    'util_mixins',
    'util_path',
    'util_platform',
    'util_stress',
    'util_str',
    'util_test',
    'util_time',
    'progiter',
    'meta',
]


__DYNAMIC__ = '--dyn' in sys.argv

if __DYNAMIC__:
    # If dynamic, imports can be autogenerated
    from ubelt._internal import dynamic_make_init
    dynamic_make_init.dynamic_import(__name__, GLOBAL_MODULES)
    _DOELSE = False
else:
    # Run the autogenerated imports
    _DOELSE = True

if _DOELSE:
    # <AUTOGEN_INIT>

    from ubelt import util_const
    from ubelt import util_decor
    from ubelt import util_dict
    from ubelt import util_cache
    from ubelt import util_io
    from ubelt import util_list
    from ubelt import util_mixins
    from ubelt import util_path
    from ubelt import util_platform
    from ubelt import util_stress
    from ubelt import util_str
    from ubelt import util_test
    from ubelt import util_time
    from ubelt import progiter
    from ubelt import meta
    from ubelt.util_const import (NoParam,)
    from ubelt.util_decor import (memoize,)
    from ubelt.util_dict import (ddict, dict_hist, dict_subset, dict_take,
                                 find_duplicates, group_items, invert_dict,
                                 map_keys, map_vals, odict,)
    from ubelt.util_cache import (Cacher,)
    from ubelt.util_io import (readfrom, writeto,)
    from ubelt.util_list import (argsort, boolmask, chunks, compress, flatten,
                                 take, unique, unique_flags,)
    from ubelt.util_mixins import (NiceRepr,)
    from ubelt.util_path import (augpath, split,)
    from ubelt.util_platform import (DARWIN, LINUX, WIN32, ensure_app_resource_dir,
                                     ensuredir, get_app_resource_dir,
                                     get_resource_dir,)
    from ubelt.util_stress import (find_nth_prime,)
    from ubelt.util_str import (CaptureStdout, codeblock, highlight_code, indent,)
    from ubelt.util_test import (DocExample, ExitTestException, doctest_package,
                                 parse_docstr_examples, parse_src_want,
                                 parse_testables,)
    from ubelt.util_time import (Timer, Timerit, timestamp,)
    from ubelt.progiter import (ProgIter,)

    # </AUTOGEN_INIT>

del _DOELSE

from __future__ import absolute_import
import sys
import six
from six.moves import zip_longest
from six import unichr
PY2 = sys.version_info[0] == 2


if not PY2:
    text_type = str
    string_types = (str,)
    binary_type = str
    unichr = chr
    int_types = (int,)
else:
    text_type = six.text_type
    string_types = (str, six.text_type)
    binary_type = bytes
    unichr = unichr
    int_types = six.integer_types

if PY2:
    
else:
    from itertools import zip_longest

if PY2:
    def implements_to_string(cls):
        cls.__unicode__ = cls.__str__
        cls.__str__ = lambda x: x.__unicode__().encode('utf-8')
        return cls
else:
    implements_to_string = lambda x: x


def force_unicode(value):
    """
    Forces a bytestring to become a Unicode string.
    """
    if PY2:
        # Python 2.X
        if isinstance(value, str):
            value = value.decode('utf-8', 'replace')
        elif not isinstance(value, six.string_types):
            value = six.text_type(value)
    else:
        # Python 3.X
        if isinstance(value, bytes):
            value = value.decode('utf-8', errors='replace')
        elif not isinstance(value, str):
            value = str(value)

    return value


def with_metaclass(meta, *bases):
    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__
        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)
    return metaclass('temporary_class', None, {})


exec_ = lambda s, *a: eval(compile(s, '<string>', 'exec'), *a)


if PY2:
    exec('def reraise(tp, value, tb):\n raise tp, value, tb')
else:
    def reraise(tp, value, tb):
        raise value.with_traceback(tb)

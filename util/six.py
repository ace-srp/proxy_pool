'''
Author: tianqi liutianqi@shoppal.ai
Date: 2024-08-29 11:35:00
LastEditors: tianqi liutianqi@shoppal.ai
LastEditTime: 2024-08-30 16:19:25
FilePath: /proxy_pool/util/six.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     six
   Description :
   Author :        JHao
   date：          2020/6/22
-------------------------------------------------
   Change Activity:
                   2020/6/22:
-------------------------------------------------
"""
__author__ = 'JHao'

import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    def iteritems(d, **kw):
        return iter(d.items(**kw))
else:
    def iteritems(d, **kw):
        return d.iteritems(**kw)

if PY3:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse

if PY3:
    from importlib import reload as reload_six
else:
    reload_six = reload

if PY3:
    from queue import Empty, Queue
else:
    from Queue import Empty, Queue


def withMetaclass(meta, *bases):
    """Create a base class with a metaclass."""

    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class MetaClass(meta):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(MetaClass, 'temporary_class', (), {})

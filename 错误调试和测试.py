# -*- encoding:utf-8 -*-
# !/usr/bin/env python3
import logging
import unittest


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
        logging.exception(e)  # 记录日志
    finally:
        print('finally...')


# 调试
# 程序会自动在pdb.set_trace()暂停并进入pdb调试环境


# 单元测试
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


def fact(n):
    '''
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be greater than one!
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    '''
    if n < 1:
        raise ValueError('n must be greater than one!')
    elif n == 1:
        return 1
    return fact(n - 1) * n


if __name__ == '__main__':
    import doctest
    doctest.testmod()

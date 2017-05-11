# -*- encoding:utf-8 -*-
# !/usr/bin/env python3


' a test module '

__author__ = 'SpartaWHY117'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()

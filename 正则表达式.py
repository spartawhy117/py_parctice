# -*- encoding:utf-8 -*-
# !/usr/bin/env python3
import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

l = re.split(r'[\s\,]+', 'a,b, c  d')

print(l)
#分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0), m.group(1), m.group(2))
#贪婪匹配
re.match(r'^(\d+)(0*)$', '102300').groups()
re.match(r'^(\d+?)(0*)$', '102300').groups()
#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()

version_1 = re.compile(r'^[\w\d]+[.]?[\w\d]+\@[\w\d]+\.\w{1,5}$')
print('版本一：', 'Found:', re.match(version_1, 'someone@gmail.com').group())
# print('        ', 'Found:',
#       re.match(version_1, 'bill...gates@microsoft.com').group())

version_2 = re.compile(r'^(<[\w\d\s]+>)?\s*([\w\d\.]+\@[\w\d]+\.[\w]+)$')
result = re.match(version_2, '<Tom Paris> tom@voyager.org').groups()
print('版本二：', 'Name:', result[0], '| Email:', result[1])

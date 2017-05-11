# -*- encoding:utf-8 -*-
# !/usr/bin/env python3
from io import StringIO
from io import BytesIO
import json
# with open('/path/to/file', 'r') as f:
#     print(f.read())


# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!')

#stringIO bytesIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

#操作文件和目录
import os

def findfile(path, str):
    if os.path.isdir(path):
        L1 = [os.path.join(path, x) for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and str in x]
        if L1:
            print(L1)
        L2 = [os.path.join(path, x) for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
        if L2:
            [findfile(x, str) for x in L2]    


# findfile(r'C:\Users\dell\Desktop\python', '.txt')


#序列化
d=dict(name='Bob',age=20,score=88)
json_str=json.dumps(d)
print(json_str)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

    
print(json.dumps(s, default=student2dict))
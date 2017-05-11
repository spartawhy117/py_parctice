# -*- encoding:utf-8 -*-
# 切片

a = [[1, 2, 3], 4, 5, 6]
b = a[:]
b[0].pop()
print(a, b)

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for i, value in enumerate(d):
    print(i, value)

# 列表生成方式
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

# 生成器
g = (x * x for x in range(10))
for n in g:
    print(n)

#yield 关键字可以控制函数成为生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
for step in f:
    print(step)


def triangles():
    ret = [1]
    while True:
        yield ret
        pre = ret[:]
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

#迭代器
#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
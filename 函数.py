# -*- encoding:utf-8 -*-
import math
# 调用函数'
n1 = 255
n2 = 100
print(hex(n2))
# 定义函数


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print('%d %d' % (my_abs(9), my_abs(-9)))


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type(a)')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type(b)')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type(c)')

    if a == 0:
        if b == 0 and c != 0:
            return '无解'
        elif b == 0 and c == 0:
            return 'x为任意数'
        else:
            return -c / b
    else:
        d = (b * b) / (4 * a * a) - c / a
        if d < 0:
            return '无实数解'
        else:
            x1 = math.sqrt(d) - (b / 2 / a)
            x2 = -math.sqrt(d) - (b / 2 / a)
            return (x1, x2)


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

# 参数调用
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


# 函数递归
# 汉诺塔 实现这个算法可以简单分为三个步骤：
# 把n-1个盘子由 A 移到 B；
# 把第n个盘子由 A 移到 C；
# 把n-1个盘子由 B 移到 C；
# 总共需要的步骤数量2^n-1
def move(n, a, b, c):
    if(n == 1):
        print(a, '->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')

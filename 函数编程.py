# 高阶函数
from functools import reduce
import functools


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, -6, abs))

# #字符串一定要返回一个新的值，内部修改影响不了外面的值


def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name


# map reduce
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2float(s):
    zeroIndex = s.find('.')
    integerStr = s[0:zeroIndex]
    floatStr = s[zeroIndex + 1:]
    integerValue = reduce(lambda x, y: x * 10 + y, map(char2num, integerStr))
    floatValue = reduce(lambda x, y: x * 10 + y,
                        map(char2num, floatStr)) / 10 ** len(floatStr)
    return integerValue + floatValue


print('str2float(\'123.456\') =', str2float('123.456'))

# filter


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
# for n in primes():
#    if n < 1000:
#        print(n)
#    else:
#        break


def is_palindrome(n):
    strValue = str(n)
    return strValue == strValue[::-1]


output = filter(is_palindrome, range(1, 1000))
# print(list(output))

# sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


LS1 = sorted(L, key=by_name)
# print(LS1)
LS2 = sorted(L, key=by_score)
# print(LS2)


# 返回函数
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

# 装饰器


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('ececute')
def now():
    print('2015-3-25')


now()


def log2(arg):
    if isinstance(arg, str):
        text = arg

        def decorator(func):
            @functools.wraps(func)
            def mk_log(*args, **kw):
                print('%s %s' % (text, func.__name__))
                func(*args, **kw)
                print('end call')
            return mk_log
        return decorator
    else:
        func = arg

        @functools.wraps(func)
        def mk_log(*arg, **kw):
            print('begin call %s' % func.__name__)
            func(*arg, **kw)
            print('end call %s' % func.__name__)
        return mk_log


@log2
def fd1():
    pass


@log2('execute')
def fd2():
    pass


fd1()
fd2()

# 偏函数
bin2dec = functools.partial(int, base=2)
print(bin2dec('0b10001'))  # 17
print(bin2dec('10001'))  # 17

hex2dec = functools.partial(int, base=16)
print(hex2dec('0x67'))  # 103
print(hex2dec('67'))  # 103

# 中文测试
print('中文')
# 字符串和编码
s1 = 72
s2 = 85
r = (s2 - s1) / s1
print('%.1f' % r)
# list and tuple
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print('%s' % L[0][0])
print('%s' % L[1][1])
print('%s' % L[2][2])
# 条件判断
height = 1.75
weight = 80.5
bmi = weight / height ** 2
if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
# 循环
L1 = ['Bart', 'Lisa', 'Adam']
for name in L1:
    print('hello,%s' % name)
#dict and set

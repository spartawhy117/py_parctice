# -*- encoding:utf-8 -*-
# 类和实例
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())
run_twice(Cat())

# 定义一个父类一个子类


class Province(object):
    def __init__(self, proname):
        self.proname = proname

    def ps(self):
        print('I am in %s' % self.proname)


class City(Province):
    def __init__(self, proname, cityname):
        self.cityname = cityname
        Province.__init__(self, proname)

    def ps1(self):
        print('I\'m in %s-%s' % (self.proname, self.cityname))

# 定义一个独立的类


class Timer(object):
    def ps(self):
        print('我不属于Province类或其子类，但我有ps方法我同样可以被调用')

    def ps1(self):
        print('我不属于Province类或其子类，但我有ps1方法我同样可以被调用')

# 定义一个函数


def f(x):
    x.ps()
    x.ps1()


# 调用部分
f(City('上海', '浦东'))
f(Timer())


#获取对象信息
#type()函数可以进行判断


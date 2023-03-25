# 魔法方法，也叫魔术方法，是类里的特殊的一些方法
# 特点：
# 1.不需要手动调用，会在合适的时机自动调用
# 2.都以 __ 开始，并以 __ 结束
# 3.方法名都是系统规定好的，写出正确的方法名才能让系统在合适的时机自己调用

class Person(object):
    # 在创建对象时，会自动调用这个方法
    def __init__(self, name, age):
        print('__init__ 方法被调用了')
        self.name = name
        self.age = age

    # 当对象被销毁时会自动调用这个方法
    def __del__(self):
        print('__del__ 方法被调用了')

    def __repr__(self):
        return '姓名：{}，年龄：{}'.format(p.name, p.age)

    def __call__(self, *args, **kwargs):
        # print('__call__ 方法被调用了')
        f = kwargs['fn']
        return f(args[0], args[1])


p = Person('张三', '18')

# 如果不做任何的修改，直接打印一个对象，是文件的 __name__.类型 内存地址

# 当打印一个对象时，会调用这个对象的 __str__ 或 __repr__ 方法
# 如果两个方法都写了，选择 __str__

print(p)

# print(repr(p))  调用内置函数 repr 会触发对象的 __repr__ 方法
# print(p.__repr__())  魔法方法一般不手动调用

print(p(1, 2, fn=lambda x, y: x * y))

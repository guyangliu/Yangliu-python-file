class Student(object):
    # 这个属性直接定义在类里，是一个元组，用于规定对象可以存在的属性
    __slots__ = ('name', 'age')

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def greeting(self):
        print('大家好我是', self.name)


# Student('张三', 18) 这段代码究竟做了什么呢？
# 1.调用 __new__ 方法，用来申请内存空间
# 2.调用 __init__ 方法传入参数，并让self指向申请好的那段内存空间，填充数据
# 3.变量s1也指向创建好的内存空间
s = Student('张三', 18)
s.greeting()

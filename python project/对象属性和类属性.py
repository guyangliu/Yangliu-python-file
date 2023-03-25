class Person(object):
    type = '人类'  # 这个属性定义在类里，函数之外，我们称之为类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('张三', 18)
print(p1.age)

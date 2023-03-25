"""
小明今年 18 岁，身高 1.75 ，喜欢 跑步，之后 吃东西，
小美今年 17 岁，身高 1.65 ，不喜欢 跑步，喜欢 吃东西，

定义类：使用class来定义一个类
类名一般需遵守大驼峰命名法，每个单词首字母都大写
1.class<类名>:
2.class<类名>(object):
"""


class Student(object):  # 关注这个类有哪些特征和行为
    # 在init方法里，以参数的形式定义特征，我们称之为属性
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # 行为定义为一个个函数
    def run(self):
        print('正在跑步')

    def eat(self):
        print('正在干饭')


# 使用Students类创建了两个事例对象stu1 stu2
# stu1和stu2同时有name,age,height属性,同时都有run和eat方法
stu1 = Student('小明', 18, 1.75)  # Students() ==> 会自动调用__init__方法
stu2 = Student('小美', 17, 1.65)

# 根据业务逻辑，让不同的对象执行不同的行为
stu1.run()
stu1.eat()

stu2.eat()

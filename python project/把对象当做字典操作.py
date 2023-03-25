class Persons(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p = Persons('Amy', '16')
p['name'] = '6'
print(p.name, p['name'])

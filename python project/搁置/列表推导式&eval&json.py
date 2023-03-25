# n = [i for i in range(10) if i % 2 == 0]
# print(n)
import json

# a = '23+9'
# print(eval(a))
i = {'name': 'yangliu', 'age': '18', 'gender': 'male'}
info = json.dumps(i)
print(info)
print(type(info))  # str类型，并非字典
down = json.loads(info)
print(down)

# print([1, 2, 3] * 3)

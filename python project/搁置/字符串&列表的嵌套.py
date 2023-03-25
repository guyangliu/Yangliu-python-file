# username = input('master，您的名字是？').ljust(8, '*')
# print('hello'.ljust(8, '*'), 'my'.ljust(8, '*'), '\n', 'master'.ljust(8, '*'), username, sep='')
import random

teachers = [1, 2, 3, 4, 5, 6]
rooms = [[], [], []]
for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)

for i, room in enumerate(rooms):
    print('第%d个房间中有，%d个老师，他们是：' % (i, len(room)), end=' ')
    for teacher in room:
        print(teacher, end=' ')
    print()

# 这是一个有注释的程序
"""
wow
它还有很多行
"""
# *a, b, c = (1, 2, 3, 4, 5)
# print(a, b, c)
# from random import *
# re = 0
for j in range(1, 10):
    i = 1
    for i in range(i, j + 1):
        print(i, '*', j, '=', i * j, sep='', end='\t')
    print()

for i in range(2, 101):
    count = 0
    for j in range(2, int(i)):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i, '是质数')
    else:
        print(i, '是合数，它可以被', count, '个数整除')

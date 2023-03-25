def add(a, b):
    """
    zhe
    :param a:
    :param b:
    :return:
    """
    a + b
    return a + b


def get_sum(*args):
    n = 0
    for i in args:
        n += i
    return n


print(get_sum(2, 3, 1, 5, 9))

# def get_sum(n):
#     if n == 0:
#         return 0
#     return n + get_sum(n - 1)
#
#
# print(get_sum(5))
def fi(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fi(n - 2) + fi(n - 1)


def round(a):
    for i in range(1,a+1):
        num = i
        print(fi(num))


c = int(input('qingshuru'))
round(c)

# 递归：方法调用本身，要有出口防止死循环
def print_num(num):
    print(num)
    if num == 1:
        return
    print_num(num - 1)


print_num(5)


def sum(num):
    if num == 0:
        return num
    return num + sum(num - 1)


print(sum(10))

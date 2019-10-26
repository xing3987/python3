# 交换两个数字
a = 6
b = 100


def chang1():
    global a, b
    c = a
    a = b
    b = c
    print("a为%d,b为%d" % (a, b))


chang1()


def change2():
    global a, b
    a = a + b
    b = a - b
    a = a - b
    # return元组类型时，可以不要小括号
    return a, b


# 接收返回的元组数据时可以直接用元组接受，省略小括号
a, b = change2()
print("a为%d,b为%d" % (a, b))

# 直接使用python独有的交换方法
a, b = (b, a)
print("a为%d,b为%d" % (a, b))



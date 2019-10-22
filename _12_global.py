# 全局变量在方法中默认是不能更改的，如果需要改变则使用global关键子修改

num = 10


def demo1():
    num = 99
    print(num)


demo1()
print(num)


def demo2():
    # 使用global关键子声明全局变量，改变值时会改变全局变量的值
    global num
    num = 99


demo2()
print(num)

"""
代码结构如下：
shebang
import模块
全局变量
函数定义
执行代码
"""

# 全局变量一般 g_或gl_ 开头


list_demo = ["x", "y", "z"]


# 一般情况全局变量在函数中值是不会被默认改变的，但是在函数中使用append可以改变全局变量的值，因为内存地址没有改变
def change4(list):
    list.append("f")


change4(list_demo)
print(list_demo)


# 针对列表变量，+=会调用extend方法,不会修改引用，所以改动了全局变量
def change5(list):
    #list += list
    list.extend(list)


change5(list_demo)
print(list_demo)

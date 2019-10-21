#全局变量在方法中默认是不能更改的，如果需要改变则使用global关键子修改

num=10

def demo1():
    num=99
    print(num)

demo1()
print(num)

def demo2():
    #使用global关键子声明全局变量，改变值时会改变全局变量的值
    global num
    num=99

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

#全局变量一般 g_或gl_ 开头
from base.helper import _helper

# 面向对象
# 使用dir()内置函数，查看对象方法(含内置方法)

gl_list = [1, 2, 3, 4]
print(dir(gl_list))

_helper.print_line("*")
"""
创建对象时，先分配空间（有了内存地址），然后会自动调用类的内置__init__方法，初始化（可以重写）
"""


# 类的命名规则：使用大驼峰规则
class Cat:
    # 哪一个对象调用的方法，self就是哪一个对象的引用
    def eat(self):
        print("小猫爱吃鱼。")

    def drink(self):
        print("小猫爱喝水。")

    def __init__(self):
        print("创建cat对象")
        self.age = 10


tom = Cat()
tom.eat()
tom.drink()
# 打印对象内存地址(主类名，十六进制内存地址)
print(tom)
# 打印十进制内存地址
addr = id(tom)
print("%d" % addr)

# 可以直接使用.***给创建出来的对象添加属性，不会对初始类产生影响，但是开发中不建议使用
tom.name = "Tom"
print(tom.name)

kitty = Cat()
print(kitty.age)

_helper.print_line("*")


# 初始化并赋值
# 对象被回收时，会触发__del__方法
class Dog:
    # 初始化对象触发
    def __init__(self, name):
        self.name = name

    # 回收对象时触发
    def __del__(self):
        print("dog 对象被回收了")

    # 类似重写tostring方法
    def __str__(self):
        return "Dog name is %s" % self.name


wan = Dog("a hua")
print(wan.name)
print(wan)
del wan
_helper.print_line("*")


"""
当多个父类有相同名称的方法时，开发时尽量避免多继承

"""


class A:
    def test(self):
        print("A --test方法")


class B:
    def test(self):
        print("B --test方法")


class C(A, B):
    def demo(self):
        print("C --demo")


xiaoc = C()
xiaoc.test()

# 查看方法执行顺序__mro__内置属性
print(C.__mro__)

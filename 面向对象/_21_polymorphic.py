# 多态
# 定义狗类
class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("遛狗。")


# 定义哮天犬类，继承狗类
class XiaoTianDog(Dog):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("在天上遛狗。")


# 定义人类
class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        #都调用了game()方法，缺因为传递的狗对象不同，产生不同结果
        dog.game()


a = Dog("狗儿")
b = XiaoTianDog("小天")
xiaomin = Person("小明")
xiaomin.game_with_dog(a)
xiaomin.game_with_dog(b)

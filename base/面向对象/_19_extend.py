# 继承

class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def sleep(self):
        print("睡")


# 继承，只要把父类写到类后面的括号中，继承多个类时用逗号分开
# （子类对象不能在自己内部不能访问父类的私有属性和方法，可以访问公有属性和方法）
# 子类可以通过访问父类的公有方法，访问共有方法里的私有属性或方法（如get(),set()方法）
class Dog(Animal):
    def bark(self):
        print("汪汪汪。")

    # 重写父类方法
    def eat(self):
        print("吃骨头。")

    # 对父类的方法进行拓展，使用super()调用父类，然后调用方法
    def sleep(self):
        super().sleep()
        print("睡的香。")


xiaowang = Dog()
xiaowang.eat()
xiaowang.sleep()

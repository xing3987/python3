# 定义私有属性，私有方法 前面添加"__"

class Person:
    def __init__(self, name, age):
        self.__age = age
        self.name = name

    def __talk(self):
        print("wa hahahahaha..")


xiaohong = Person("xiaohong", 18)
# 私有属性外部不能直接访问，会报错
# print(xiaohong.name,xiaohong.__age)
# 私有方法外部不能直接访问，会报错
# xiaohong.__talk()

# 通过分析解析器，在私有属性前加“_类名”就可以访问了，所以python是伪私有的方法和属性
print(xiaohong._Person__age)
xiaohong._Person__talk()

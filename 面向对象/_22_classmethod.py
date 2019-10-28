# 类属性，类方法，静态方法

class Tool:
    # 定义类属性，所有类共用
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1  # 赋值类属性用[实例类.属性名]

    # 静态方法不需要传递任何类有关参数，不能使用类属性
    @staticmethod
    def help():
        print("工具的使用帮助。")

    # 使用@classmethod注解定义类方法，所有实例类公用,第一个参数为类本身
    @classmethod
    def count_tool(cls):
        # 类方法可以调用类属性cls.属性名
        print("工具的数量为%s" % cls.count)


tool1 = Tool("tool1")
print(Tool.count)

tool2 = Tool("tool2")
# 虽然使用[实例类.属性名]也可以获得结果；但是当实例的属性和类属性同名时
# 会输出实例属性，这样就不好区分；所以实际开发中尽量使用[类.属性名]
print(tool2.count)

# 直接使用[类.类方法]调用类方法
Tool.count_tool()

# 直接使用[类.类方法]调用静态方法
Tool.help()

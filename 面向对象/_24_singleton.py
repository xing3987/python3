# 单例模式，利用__new__固有方法

class SingleTon:
    # 定义一个属性，记录对象的引用
    instance = None
    gl_init_flag = False

    # 重写new方法
    def __new__(cls, *args, **kwargs):
        # 如果对象的引用是空，返回一个新的对象，否则返回原对象引用
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    # 扩展，让初始化也只执行一次
    def __init__(self):
        # 判断是否初始化，如果执行过初始化直接返回
        if self.gl_init_flag:
            return

        print("执行初始化操作，赋值等。。")

        self.gl_init_flag = True


single1 = SingleTon()
print(single1)
single2 = SingleTon()
print(single2)

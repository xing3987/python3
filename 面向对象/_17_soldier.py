# 士兵突击

# 定义枪类
class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if (self.bullet_count > 0):
            print("突突突。。")
            self.bullet_count -= 1
            print("还有%d发子弹。" % self.bullet_count)
        else:
            print("没有子弹了，快点逃跑呀。")
            return


# 定义士兵类
class Soldier:
    def __init__(self, name):
        self.name = name
        # 初始化属性为空
        self.gun = None

    def fire(self):
        # 判断是否有枪,None使用is判断
        if self.gun is None:
            print("给把枪吧..")
            return
        if self.gun.bullet_count == 0:
            print("枪木有子弹啦，请给枪上膛鸭。。")
            return
        print("冲鸭。。。%s" % self.name)
        self.gun.shoot()


ak47 = Gun("ak47")
xiaoming = Soldier("xiaoming")
# 设置属性为新的对象
xiaoming.gun = ak47
# xiaoming.gun.add_bullet(100)
xiaoming.fire()

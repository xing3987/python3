# 摆放家具

# 家具类
class HouseItem:

    # 定义家具初始化需要的属性，名字，面积
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具名为%s，占地面积为%.02f." % (self.name, self.area)


# 房子类
class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("房子的户型为%s,总面积为%.02f平,剩余面积为%.02f平,家具名称%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        # 判断家具面积和剩余面积大小
        if self.free_area > item.area:
            self.item_list.append(item.name)
            self.free_area -= item.area
        else:
            print("家具%s面积过大，剩余面积不足。" % item.name)
            return


bed = HouseItem("床", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
car = HouseItem("拖车", 100)
print(bed, chest, table)

xiaoming = House("三室户", 100)
xiaoming.add_item(bed)
xiaoming.add_item(table)
xiaoming.add_item(chest)
xiaoming.add_item(car)
print(xiaoming)

# 字典的定义
xiaoming_dict = {"name": "小明",
                 "age": 18,
                 "height": 1.75}
# 字典是无序的
print(xiaoming_dict)

# 字典的取值
print(xiaoming_dict["name"])

# 字典的赋值,增加，修改
xiaoming_dict["age"] = 19
xiaoming_dict["sex"] = "M"
print(xiaoming_dict)

# 删除(如果key不存在会报错)
xiaoming_dict.pop("name")
print(xiaoming_dict)

# 合并字典(如果被合并的字典中含有被合并的key，会被覆盖)
xiaoming_weight = {"weight": 65,
                   "sex": "F"}
xiaoming_dict.update(xiaoming_weight)
print(xiaoming_dict)

# 清空
# xiaoming_dict.clear()
# print(xiaoming_dict)

# 遍历
for k in xiaoming_dict:
    print("%s -> %s" % (k, xiaoming_dict[k]))

# 多重字典
ren_info = [{"name": "小明", "age": 18, "height": 1.75},
            {"name": "小红", "age": 15, "height": 1.65}]

for info in ren_info:
    print(info)
    for k in info:
        print("%s -> %s" % (k, info[k]))

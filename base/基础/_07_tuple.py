single_turple = (3)
print(type(single_turple))

single_turple = (3,)
print(type(single_turple))

# list tuple相互转换
num_list = [1, 2, 4, 5]
num_tuple = tuple(num_list)
print(num_tuple)

num_list = list(num_tuple)
print(num_list)

info_tuple = ("小明", 16, 1.85)
print("%s 年龄是 %d,身高为 %.02f." % info_tuple)

#循环变量
for info in info_tuple:
    print(info)

#取值和去索引
print(info_tuple[0])
print(info_tuple.index("小明"))

from base.helper import _helper

_helper.print_line("*")
#切片(同string规则)
print(info_tuple[1:3])

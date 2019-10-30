from helper import _helper
"""
a.增加
insert(索引，数据) ：在指定位置插入数据
append(数据) ：在末尾追加数据
extend(列表2) ：将列表2的数据追加到列表中
b.修改
列表[index]=数据 ：修改指定索引的数据
c.删除
del 列表[index]:删除指定索引的数据->del name_list[0]
列表.remove(数据)：删除第一个出现的指定数据
列表.pop: 删除末尾数据
列表.pop(index): 删除指定索引的数据
列表.clear :清空列表
d.统计
len(列表)：列表长度
列表.count(数据)：数据在列表中出现的次数
e.排序
列表.sort():升序排序
列表.sort(reverse=True):降序排序
"""

name_list = ["Marry", "Tom", "Kitty", "Tom"]
print(len(name_list))

del (name_list[0])
print(name_list)

name_list.append("Jason")
name_list.remove("Kitty")

print(name_list.count("Tom"))

name_list.remove("Tom")
print(name_list)

name_list.sort()
print(name_list)
name_list.sort(reverse=True)
print(name_list)
name_list.reverse()
print(name_list)


#遍历
for name in name_list:
    print(name)


_helper.print_line("*")

#切片(同string规则)
print(name_list[1:2])

# 符号“+”会生成新的列表
name_list + ["Tommy"]
print(name_list)
# extend会追加
name_list.extend(["Jetty"])
print(name_list)
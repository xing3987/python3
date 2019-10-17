name_list = ["Marry", "Tom", "Kitty", "Tom"]

# for 循环外的else表示整个for循环结束还没有break跳出，则会执行
for name in name_list:
    print(name)
    aim = "Kitty"
    if (name == aim):
        print("找到了%s" % aim)
        break
else:
    print("没有找到。。")




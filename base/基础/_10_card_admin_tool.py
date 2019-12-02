# 名片管理系统工具类
from base.helper import _helper

card_list = []


def add():
    """
    添加名片信息
    """
    name_str = input("姓名：")
    tel_str = input("电话：")
    qq_str = input("QQ：")

    name_dirt = {}
    name_dirt["name"] = name_str
    name_dirt["tel"] = tel_str
    name_dirt["qq"] = qq_str
    card_list.append(name_dirt)
    print("添加 %s的名片成功。。" % name_str)


def show_all():
    """
    显示名片信息
    """
    if len(card_list) > 0:
        for key in ("姓名", "电话", "QQ"):
            print(key, end="\t\t")
        print()
        _helper.print_line("-")
    else:
        print("名片夹中没有数据，请创建。")
        return
    for name_dirt in card_list:
        print("%s\t\t%s\t\t%s" % (name_dirt["name"], name_dirt["tel"], name_dirt["qq"]))


def find():
    name = input("请输入要查找的姓名：")
    for name_dirt in card_list:
        if name == name_dirt["name"]:
            print("%s\t\t%s\t\t%s" % (name_dirt["name"], name_dirt["tel"], name_dirt["qq"]))
            control = input("请选择操作功能：【1】.修改信息  【2】.删除该数据 【其他】.返回\t")
            if control == "1":
                update_card(name_dirt)
            elif control == "2":
                remove_card(name_dirt)
            break
    else:
        print("没有查询到您要的数据。")


def update_card(name_dirt):
    name_str = input("姓名：")
    tel_str = input("电话：")
    qq_str = input("QQ：")
    if name_dirt != "":
        name_dirt["name"] = name_str
    if tel_str != "":
        name_dirt["tel"] = tel_str
    if qq_str != "":
        name_dirt["qq"] = qq_str
    print("修改成功。")


def remove_card(name_dirt):
    card_list.remove(name_dirt)
    print("删除成功。")

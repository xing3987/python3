#! /usr/bin/python3

# 使用“#! python3路径在linux中再赋予可执行-x权限，则该文件可以在Linux中直接执行”
from 基础 import _10_card_admin_tool
import helper

# 设计一个名片管理系统
while (True):
    helper.print_line("*")
    print("欢迎使用【名片管理系统】v1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")
    helper.print_line("*")

    control = input("请选择操作功能:\n")
    if (control == "1"):
        helper.print_line("-")
        print("功能：新建名片")
        _10_card_admin_tool.add()
    elif (control == "2"):
        helper.print_line("-")
        print("功能：显示全部名片")
        _10_card_admin_tool.show_all()
    elif (control == "3"):
        helper.print_line("-")
        print("功能：查询名片")
        _10_card_admin_tool.find()
    elif (control == "0"):
        break
    else:
        print("请输入正确的操作。")

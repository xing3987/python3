from 面向对象._25_exception import input_data

"""
导入模块或包：
import *.py
import *.py as **
from package import *.py
from package import *.py as **

局部导入方法或类
from package.*.py import [method] as **
"""
# input_data()

"""
__name__属性可以做到，测试模块的代码只在本身测试情况下被运行
而被其他模块导入时不会执行
"""


def say_hello():
    print("hello hello...")


if __name__ == "__main__":
    print("测试代码块。")
    say_hello()

"""
创建包时，默认包下要创建一个__init__.py的文件
内部暴露出给其他模块使用的文件
该文件内容示例：
from . import **

# 其他模块通过import package就可以调用该模块，
# 也可以from package import *.py文件导入特定模块使用
"""

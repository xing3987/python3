# 制作发布压缩包步骤
"""
1 创建setup.py文件

from distutils.core import setup

setup(name="package", #包名
    version="1.0",
    description="发布模块描述信息",
    long_description="发布模块描述信息(完整)",
    author="作者",
    author_email="作者邮箱",
    url="作者主页",
    py_modules=["module","module"]) #主要信息，模块内容,每个*.py文件


2 构建模块(在编译环境下)
python3 setup.py build

3 生成发布压缩包
python3 setup.py sdist


4 其他人拿到文件，安装到pyhon中
sudo python3 setup.py install

5.使用
import package.module
"""

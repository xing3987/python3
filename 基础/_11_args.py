from helper import _helper

# 使用id()查看内存地址
a = 1
print("%s 的地址为：%s" % (a, id(a)))

b = "hello"
print("%s 的地址为：%s" % (b, id(b)))

"""
可变和不可变类型
1.不可变类型，内存中的数据不允许被修改（修改后改变了地址）
数组类型
字符串
元组

不可变类型可以作为key,可以使用hash算法

2.可变类型，内存中的数据可以被修改（内存地址不会改变，但是使用赋值语句重新赋值，会改变地址）
列表
字典

可变类型不可以作为key,不可以使用hash算法
"""

c = (1, 2, 3)
print(hash(c))


# 设置方法的默认值，有默认值的参数放在方法末尾，不然会报错
def print_info(name, gender=True):
    gender_text = "man"
    if not gender:
        gender_text = "girl"
    print("%s 是 %s" % (name, gender_text))


print_info("lili")

"""
参数前面加*可以接收元组数据
参数前面加**可以接收字典类型数据
"""


def test_args(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


_helper.print_line("*")
test_args(1)
_helper.print_line("*")
test_args(1, 2, 3, 4)
_helper.print_line("*")
test_args(1, 2, 3, 4, name="tom", gender="F")
_helper.print_line("*")

gl_tuple = [1, 2, 3]
gl_dir = {"name": "tom", "gender": "F"}

#直接传递元组或字典，得不到预期结果，需要拆包，前面加*（元组），**（字典）
test_args(1, gl_tuple, gl_dir)
_helper.print_line("*")
test_args(1, *gl_tuple, **gl_dir)


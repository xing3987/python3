import keyword

print('hello')
print("你好")

name = '小明'
age = 18
sex = True  # True算术运行中为1，False为0
height = 1.75
weight = 75

print(age + sex)
print(name * 10)  # 得到多个整数

print(type(float(age)))

'''
%s 字符串
%d 有符号的十进制整数 %06d表示显示6位数,不足用0占位
%f 浮点数%.02f表示小数点后只显示两位
%% 输出%
'''
'''
apple = int(input("请输入。。\n")) #input 默认格式为str
price = float(input("价格。。\n"))
money = int(apple) * float(price)
print("苹果%01d个，单价为%.02f,总价为%.02f" % (apple, price, money))
'''

# 查看所有关键字
print(keyword.kwlist)
"""
自定义生成器
"""


# 创建一个方法用于获取斐波那契数据
# 0 1 1 2 3 5 8 13...
def fibonacci(count):
    a = 0
    b = 1
    for i in range(count):
        yield a  # 使用yield创建一个生成器
        a, b = b, a + b


def main():
    # 第一种方式，创建一个生成器
    num = (i * 2 for i in range(10))
    print(num)
    # 使用生成器
    for i in num:
        print("%d \t" % i, end="")
    print()

    nums = fibonacci(10)
    # 使用生成器
    for i in nums:
        print("%d \t" % i, end="")


if __name__ == "__main__":
    main()

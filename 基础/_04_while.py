i = 0
while i <= 5:
    print("i 的值为 %d." % i)
    i += 1
    if (i == 3):
        break
print("循环结束")

# continue关键字，如果运行到continue时，会跳过循环中的continue之后的内容
j = 0
while j <= 5:
    j += 1
    if (j == 3):
        continue
    print("j 的值为 %d." % j)
print("循环结束")

# 九九乘法表
print("",end="") #如果结果不为“”时不会换行
i = 1
j = 1
while j <= 9:
    while i <= j:
        print("%d * %d = %d \t" % (i, j, i * j), end="")
        i += 1
    print()
    j += 1
    i = 1

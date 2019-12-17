from matplotlib import pyplot as plt

# x绘制2~26 每隔2个数绘制一个点(含头不含尾)
x = range(2, 26, 2)
# y轴12个点
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 绘图
plt.plot(x, y)
# 显示
plt.show()

from matplotlib import pyplot as plt

# x绘制2~26 每隔2个数绘制一个点(含头不含尾)
x = range(2, 26, 2)
# y轴12个点
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 设置图片大小
plt.figure(figsize=(10, 5), dpi=80)

# 绘图
plt.plot(x, y)

# 重新设置x轴的刻度
plt.xticks(range(1, 30))  # 间隙为1
# 重新设置y轴的刻度（需要调整刻度间隙为2）
y_ticks = [i * 2 for i in range(5, 15)]  # 创建刻度数组
plt.yticks(y_ticks)

# 显示
plt.show()

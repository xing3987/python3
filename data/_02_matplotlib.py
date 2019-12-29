"""
如果a表示10点到12点的每一分钟的气温，绘制折线图观察每分钟气温的变化情况
a=[random.randint(20,35) for i in range(120)]
"""

import random

from matplotlib import pyplot as plt


def main():
    # 绘制x,y的点位坐标信息
    y = [random.randint(20, 35) for i in range(120)]  # 每分钟气温
    x = range(0, 120)  # 时间
    # 设置图片大小
    plt.figure(figsize=(10, 7), dpi=80)
    # 绘图
    plt.plot(x, y)
    """
    # 重新设置x轴的刻度
    # x_ticks = [i * 5 for i in range(0, 25)]  # 创建刻度数组
    x_ticks = (list(x))[::5]  # 默认不含最后一个刻度120,使用步长分隔数组
    x_ticks.append(120)  # 加上最后一个刻度
    """
    """
    # 设置字体
    # 第一种方法
    from matplotlib import rc
    # font = {'family': 'MicroSoft YaHei', 'weight': 'bold', 'size': 'larger'}
    # rc("font", **font)
    rc("font", family='MicroSoft YaHei', weight='bold')
    #第二种方法
    from matplotlib import font_manager
    myfont = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")#通过ttc文件创建字体格式
    plt.xticks(list(x)[::5], x_ticks[::5], rotation=45, fontproperties=myfont)
    """
    # 第三种方法
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 调整显示时间文字
    x_ticks = ["10点{}分".format(i) for i in range(0, 60)]
    x_ticks += ["11点{}分".format(i) for i in range(0, 60)]
    plt.xticks(list(x)[::5], x_ticks[::5], rotation=45)
    # 添加描述信息
    plt.xlabel("时间")
    plt.ylabel("温度 单位（℃）")
    plt.title("10点到12点每分钟的气温变化情况")
    # 显示图片
    plt.show()


if __name__ == "__main__":
    main()

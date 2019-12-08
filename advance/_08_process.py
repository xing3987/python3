"""进程"""
"""
进程和线程的区别
进程：QQ多开
线程：一个QQ多个聊天窗口
进程的运行会拷贝代码和资源，更占用CPU。
进程之间是相互独立的，线程之间会共享全局变量。
进程之间要相互通信，可以使用消息队列
"""

import multiprocessing
import time


# 多线程的使用threading


def sing():
    """唱歌5秒"""
    for i in range(5):
        print("正在唱歌。。。。")
        time.sleep(1)


def dance():
    """跳舞5秒"""
    for i in range(5):
        print("正在跳舞。。。。")
        time.sleep(1)


def main():
    t1 = multiprocessing.Process(target=sing)
    t2 = multiprocessing.Process(target=dance)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()

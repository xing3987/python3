import threading
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
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    # 查看正在运行的所有线程
    print(threading.enumerate())


if __name__ == "__main__":
    main()

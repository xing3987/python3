import threading

import time

"""
线程锁
"""
my_lock = threading.Lock()

# 定义一个全局变量
g_num = 0


def test1(num):
    global g_num
    # 加线程锁，如果已经有锁则会阻塞在这里
    # my_lock.acquire()
    for i in range(num):
        my_lock.acquire()
        g_num += 1
        my_lock.release()
    # my_lock.release()
    print("in test1 g_num=%d..." % g_num)


def test2(num):
    global g_num
    # 加线程锁，如果已经有锁则会阻塞在这里
    # my_lock.acquire()
    for i in range(num):
        my_lock.acquire()
        g_num += 1
        my_lock.release()
    # my_lock.release()
    print("in test2 g_num=%d..." % g_num)


def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))
    t1.start()
    t2.start()
    time.sleep(2)


if __name__ == "__main__":
    main()

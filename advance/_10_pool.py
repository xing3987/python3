"""
进程池的使用：为了不要重复创建进程消耗大量的cpu资源
"""
import os
import random
import time
from multiprocessing import Pool


def worker(msg):
    t_start = time.time()
    print("%s————————开始执行，进程号为%d" % (msg, os.getpid()))
    # 休眠0-2秒
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


def main():
    # 创建一个进程池，其中进程的最大数量为3
    po = Pool(3)
    print("----start----")
    for i in range(0, 10):
        # 启用进程池，执行进程
        po.apply_async(worker, (i,))

    po.close()  # 关闭线程池，关闭后po不再接受新的请求
    po.join()  # 等等po中所有的子进程执行完成，必须放在close语句之后
    print("-----end-----")


if __name__ == "__main__":
    main()

"""
使用gevent实现多任务(协成)
gevent其实就是在yield上的进一步封装
"""
import time

import gevent
from gevent import monkey

# 有耗时操作时直接使用补丁的方式调用gevent，
# 该方法会把耗时操作自动转换为gevent中自己实现的模块
monkey.patch_all()


def task(n, name):
    for i in range(n):
        print("%s -- %d" % (name, i))
        time.sleep(0.1)


def main():
    # 使用gevent.joinall把所有需要同步的任务加入到gevent中
    gevent.joinall([
        gevent.spawn(task, 10, "work1"),
        gevent.spawn(task, 10, "work2")
    ])


if __name__ == "__main__":
    main()

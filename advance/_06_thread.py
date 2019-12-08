import threading
import time


# 自定义线程，继承Thread,适合线程比较复杂时

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            msg = "当前线程名为：%s @ %d" % (self.name, i)
            print(msg)
            time.sleep(1)


def main():
    t1 = MyThread()
    t1.start()


if __name__ == "__main__":
    main()

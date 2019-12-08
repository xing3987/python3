import multiprocessing

"""使用队列完成进程间的通信"""


def download_from_web(q):
    """下载数据"""
    data = [11, 22, 33, 44, 55]
    # 向队列中写入数据
    for temp in data:
        q.put(temp)


def analysis_data(q):
    print("处理数据。。。")
    waitting_analysis_data = list()
    # 获取队列中的数据，如果队列中没有了数据则结束
    while True:
        waitting_analysis_data.append(q.get())
        if q.empty():
            break

    print(waitting_analysis_data)


def main():
    # 创建队列用于数据传输
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()

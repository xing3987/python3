"""
使用进程池，实现文件夹的拷贝
"""
import os
import multiprocessing


def copy_file(queue, file_name, old_folder_name, new_folder_name):
    """在该方法中完成文件的复制"""
    print("===模拟复制文件：从%s到%s,文件名是%s"
          % (old_folder_name, new_folder_name, file_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()
    # 把copy完成的文件丢如队列中
    queue.put(file_name)


def main():
    # 1.获取用户要copy的文件夹的名字
    old_folder_name = input("请输入需要copy的文件夹的名字：")

    # 2.创建一个新的文件夹mkdir()
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    # 3.获取文件夹的所有的待copy的文件名字listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)

    # 4.创建一个队列用于统计任务进度
    q = multiprocessing.Queue()

    # 5.创建一个进程池，其中进程的最大数量为5，向进程池中添加copy文件的任务
    po = multiprocessing.Pool(5)
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name,
                                        old_folder_name, new_folder_name))

    po.close()

    # 显示任务进度
    all_file_num = len(file_names)
    finish_copy_num = 0

    # po.join() 不使用主进程的等待方法，使用wile--True阻塞等待主进程结束
    while True:
        file_name = q.get()
        # print("已经完成copy：%s" % file_name)
        finish_copy_num += 1
        # %%只显示一个%,使输出在一行显示end="",使输入一直从头开始"\r"
        print("\r拷贝的进度为：%0.2f %%" % (finish_copy_num / all_file_num) * 100, end="")
        if finish_copy_num >= all_file_num:
            break

    print()


if __name__ == "__main__":
    main()

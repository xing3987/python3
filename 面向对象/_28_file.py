import os

"""
文件操作
1 open 打开文件
    open("文件名","打开方式",编码格式)
    r:只读，文件不存在抛异常
    w:只写，文件不存在创建新文件
    a:追加写入，文件不存在创建新文件
    r+:读写方式打开，文件的指针会在开头，如果文件不存在，抛异常
    w+:读写方式打开，文件存在则覆盖，文件不存在创建新文件
    a+:读写方式打开，文件存在末尾追加，文件不存在创建新文件
2 read
    read()读取全文件
    readline()读取一行
3 write

4 close
"""

f1 = open("_27_setup.py", encoding='utf-8')

# 读取整个文件
# text = f1.read()
# print(text)

# 一行行读取文件
# while True:
#     line = f1.readline()
#     if not line:
#         break
#     print(line)

# 文件复制
f2 = open("copy.py", "w", encoding="utf-8")
while True:
    line = f1.readline()
    if not line:
        break
    f2.write(line)
f2.flush()
f2.close()

f1.close()

"""
os文件管理模块
文件操作
rename   os.rename(源文件，目标文件名)
remove   os.remove(源文件)
目录操作
listdir：查看目录列表;os.listdir(目录)
mkdir：创建目录;os.mkdir(目录)
rmdir：删除目录;os.rmdir(目录)
getcwd：获取当前目录;os.getcwd()
chdir：修改工作目录;os.chdir(目标目录)
path.isdir：判断是否是文件;os.path.isdir(文件路径)
"""

os.remove("copy.py")



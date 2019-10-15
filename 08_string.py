# 字符串操作
hello_str = "hello yellow"

# 统计出现次数(字符串不存在返回0)
print(hello_str.count("llo"))

# 统计子字符串出现位置（字符串不错在会报错）
print(hello_str.index("o"))

"""
字符串的方法：
string.capitalize;  string.format;          string.islower
string.lower;       string.rpartition;      string.title;
string.format_map;  string.isnumeric;       string.lstrip
string.rsplit;      string.translate;       string.center
string.index;       string.isprintable;     string.maketrans
string.rstrip;      string.upper;           string.count
string.isalnum;     string.isspace;         string.partition
string.split;       string.zfill;           string.encode
string.isalpha;     string.istitle;         string.replace
string.splitlines;  string.endswith;        string.isdecimal
string.isupper;     string.rfind;           string.startswith
string.expandtabs;  string.isdigit;         string.join
string.rindex;      string.strip;           string.find
string.isidentifier;string.ljust;           string.rjust
string.swapcase;    string.casefold
"""

space_str = "    \n\r\t"
print(space_str.isspace())

num = "123"
print(num.isdecimal())

print(hello_str.index("llo"))
# find字符串不存在返回-1,index会报错
print(hello_str.find("lloo"))

# replace不会改变原有字符串，会返回一个替换后的字符串
print(hello_str.replace("yellow", "python"))
print(hello_str)

import helper

helper.print_line("*")

# 文本对齐
poem = ["登鹳雀楼",
        "王之涣　唐 \t\n",
        "白日依山尽，",
        "黄河入海流。",
        "欲穷千里目，",
        "更上一层楼。"]

# 第一个参数总长度，第二个为默认填充符号
# strip()去除前后空白
for poem_str in poem:
    print("|%s|" % poem_str.strip().center(16, "　"))
'''
poem.ljust() 
poem.rjust()
print(poem)
poem.center()
print(poem)
'''

# 拆分和拼接
hello_list = hello_str.split(" ")
print(hello_list)
hello_join = " ".join(hello_list)
print(hello_join)

# 切片 str[开始索引：结束索引：步长]，含前不含后
print(hello_join[2:5:1])
print(hello_join[3:])
print(hello_join[:3])
#从后往前逆序切片
print(hello_join[-1:5:-1])

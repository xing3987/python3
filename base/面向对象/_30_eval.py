# 执行函数

input_str = input("请输入计算题\n")

print(eval(input_str))

# 警慎使用eval()函数，容易产生漏洞，特别是eval(input())直接执行用户输入的内容

#系统自带执行指令的方法
#__import__('os').system('pwd')

# 如果input中输入导入os模块，执行系统命令就太可怕了：
#   eval("__import__('os').system('pwd')")


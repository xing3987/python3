age = 2

if age >= 18:
    print("可以去网吧。")
elif age > 5:
    print("回家写作业。")
else:
    print("宝宝快爬。")

# not关键子
flag = True
if not flag:
    print("hello.")
else:
    print("gogo.")

print("##################")

'''
人机对战剪刀石头布1.剪刀，2.石头，3.布
'''
def getstr(data): #定义输入和文字对应的方法
    if (data == 1):
        return "剪刀";
    elif (data == 2):
        return "石头";
    else:
        return "布";

people = int(input("请出拳。。1.剪刀，2.石头，3.布 \n"))

import random
computer=random.randint(1,3)  #random两边都包含
print(computer)
comstr=getstr(computer)
prostr=getstr(people)

if ((people == 1 and computer==2) or (people == 2 and computer==3)
        or (people == 3 and computer==1)):
    print("电脑出拳:%s,您出拳:%s,您输了!" %(comstr,prostr))
elif (people == computer):
    print("电脑出拳:%s,您出拳:%s,平局!" % (comstr, prostr))
else:
    print("电脑出拳:%s,您出拳:%s,您胜利了!" % (comstr, prostr))


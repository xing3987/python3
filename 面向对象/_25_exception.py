def input_data():
    try:
        num = int(input("请输入一个整数。"))
        result = num / 8
        print(result)

    # 扑捉特定异常
    except ZeroDivisionError:
        print("除0错误。")
    except ValueError:
        print("请输入正确的整数。")

    # 扑捉未知的异常，并做出处理
    except Exception as result:
        print("其他异常%s。" % result)

    else:
        print("没有异常才会执行的代码。")
    finally:
        print("无论是否有异常，最终都会执行的代码。")


# input_data()

# 主动抛出异常
def raise_exception():
    pwd = input("请输入密码:")

    if len(pwd) >= 8:
        return pwd
    else:
        # 创建一个异常并抛出
        ex = Exception("密码长度小于8位数")
        raise ex

if __name__=="__main__":
    try:
        print(raise_exception())
    except Exception as result:
        print("出现异常:%s." % result)

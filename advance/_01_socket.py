import socket


def main():
    # 1.创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.使用套接字收发数据socket.sendto("内容"(bytes),目标ip及端口)
    #   发送内容有两种b"string","string".encode("utf-8")
    while True:
        datas = input("请输入要发送的数据：")
        udp_socket.sendto(datas.encode("utf-8"), ("localhost", 9999))

    # 3.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()

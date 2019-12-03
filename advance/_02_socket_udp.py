import socket


# udp服务端
def main():
    # 1.创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定一个本地端口
    localaddr = ("", 9999)
    udp_socket.bind(localaddr)
    # 3.接收数据
    while True:
        all_msg = udp_socket.recvfrom(1024)
        # 接收的信息是一个元组(b'hello', ('127.0.0.1', 56208))
        msg = all_msg[0].decode("UTF-8")
        ip = all_msg[1][0]
        port = all_msg[1][1]
        print("接收到的信息为:%s,发送方的ip为:%s和端口为:%d" % (msg, ip, port))

    # 3.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()

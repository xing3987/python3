from socket import *


# tcp客户端（下载文件客户端）
def main():
    # 1.创建socket默认就是tcp
    # tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket = socket()
    # 2.连接服务器
    server_ip = input("请输入要连接的服务器ip:")
    server_port = input("请输入要连接服务器的port:")
    server_addr = (server_ip, int(server_port))
    tcp_client_socket.connect(server_addr)
    # 3.发送数据
    file_name = input("请输入要下载的文件名：")
    tcp_client_socket.send(file_name.encode("utf-8"))
    # 4.接收数据
    recv_data = tcp_client_socket.recv(1024 * 1024)
    if recv_data:
        # 如果接收到了数据，则保存在一个文件中
        #使用with ..open... as... 会自动处理文件流的开关
        with open("[recv]" + file_name, "wb") as f:
            f.write(recv_data)
    # 5.关闭连接
    tcp_client_socket.close()


if __name__ == "__main__":
    main()

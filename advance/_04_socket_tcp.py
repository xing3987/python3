from socket import *


# tcp服务端（文件服务器）
def send_file_2_client(client_sock):
    # 1.接收客户端发送过来的文件名
    file_name = client_sock.recv(1024).decode("utf-8")
    print("收到客户端发送的消息,需要下载的文件为：%s" % file_name)
    # 2.打开这个文件，读取数据
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ex:
        print("没有找到该文件：%s" % file_name)

    if file_content:
        client_sock.send(file_content)
    else:
        client_sock.send(("没有找到该文件：%s" % file_name).encode("utf-8"))


def main():
    # 1.创建socket默认就是tcp
    tcp_server_socket = socket()
    # 2.绑定本地信息
    tcp_server_socket.bind(("", 9988))
    # 3.改变模式为监听模式(设定同一时间可以有多个客户端连接)
    tcp_server_socket.listen(128)
    while True:
        # 4.等待连接,返回类型是个元组
        client_sock, addr = tcp_server_socket.accept()
        print("有一个客户端连接上，地址为%s" % str(addr))
        # 5.可以回复信息给客户端
        # client_sock.send("hello..".encode("utf-8"))
        # 5.收到客户端发来的文件名，发送文件给客户端
        send_file_2_client(client_sock)
        # 6.关闭连接
        client_sock.close()

    tcp_server_socket.close()


if __name__ == "__main__":
    main()

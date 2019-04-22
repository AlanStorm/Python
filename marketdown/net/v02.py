import socket


# 模拟客户端的函数
def clicentFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "I love jingjing"
    # 发送的数据必须是bytes格式
    data = text.encode()

    # 发送
    sock.sendto(data, ("127.0.0.1", 7852))

    receive_data, receive_addr = sock.recvfrom(200)

    receive_data = receive_data.decode()

    print(receive_data)


if __name__ == '__main__':
    clicentFunc()

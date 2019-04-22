# socket模块负责socket编程
import socket


# 模拟服务器的函数
def serverFunc():
    # 1.建立socket
    # socket.AF_INET：使用ipv4协议族
    # socket.SOCK_DGRAM：使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定ip和port
    # 127.0.0.1：这个ip地址代表的是机器本身
    # 7852：随意指定的端口号
    # 地址是一个tuple类型，(ip, port)
    addr = ("127.0.0.1", 7852)
    sock.bind(addr)

    # 接受对方消息
    # 等待方式为死等，没有其他可能性
    # recvfrom接受的返回值是一个元组，前一项表示数据，后一项表示地址
    # 参数的含义是缓冲区大小
    # rst = sock.recvfrom(500)
    receive_data, receive_addr = sock.recvfrom(200)
    print(receive_data)
    print(type(receive_data))

    # 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # decode默认参数是utf8
    text = receive_data.decode()
    print(type(text))
    print(text)

    # 给对方返回消息
    rsp = "Ich hab kek kkk "

    # 发送的数据需要编码称bytes格式
    send_data = rsp.encode()
    sock.sendto(send_data, receive_addr)


if __name__ == '__main__':
    print('Start server...')
    serverFunc()
    print('End server')

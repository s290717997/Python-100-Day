
"""
最基本的客户端
（1）创建套接字，默认为IPv4和TCP协议
  client = socket()
（2）连接服务器IP和端口
client.connect(('192.168.1.201', 6789))
（3）数据通信，发送或者接收，默认也是阻塞的
 print(client.recv(1024).decode('utf-8'))
（4）关闭连接
 client.close()
"""
from socket import socket

def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器(需要指定IP地址和端口)
    client.connect(('192.168.1.201', 6788))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
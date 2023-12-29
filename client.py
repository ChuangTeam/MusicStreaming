import socket
class client:
    def __init__(self):
        # 1.创建socket
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip='127.0.0.1', port=7788):
        # 2. 链接服务器
        self.server_addr = (ip, port)
        self.tcp_socket.connect(self.server_addr)
        print('连接到')


    def send_data(self, massage):
        self.tcp_socket.send(massage.encode("gbk"))

    def close(self):
        # 4. 关闭套接字
        self.tcp_socket.close()
        print('client端已关闭')


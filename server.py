import socket


class server:
    def __init__(self):

        # 创建socket
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcp_server_socket.setblocking(False)
        self.tcp_server_socket.settimeout(0.0)

        self.conn_que = []  # 客户端套接字队列
    def init(self, ip='127.0.0.1', port=7788):
        # 本地信息
        self.address = (ip, port)

        # 绑定
        self.tcp_server_socket.bind(self.address)

        self.tcp_server_socket.listen(128)
        print('开启服务端')

    def waitNewClient(self):
        # 等待新的客户端连接
        print('等待新的客户端连接')
        try:
            self.client_socket, self.clientAddr = self.tcp_server_socket.accept()
            print(f'连接到{self.clientAddr[0]}')
            self.clientAddr.setblocking(False)
            self.conn_que.append(self.clientAddr)
        except Exception as e:  # 无连接pass继续查询
            pass

    def listener(self):
        # 接收对方发送过来的数据
        try:
            recv_data = self.client_socket.recv(1024)  # 接收1024个字节
            if recv_data:
                print('接收到的数据为:', recv_data.decode('gbk'))
                return recv_data.decode('gbk')
        except Exception as e:  # 无连接pass继续查询
            pass
    def close(self):
        self.tcp_server_socket.close()
        print('server端已关闭')

if __name__ == '__main__':
    ser = server()
    ser.init(ip='192.168.3.181', port=7788)

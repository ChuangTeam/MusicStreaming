import tkinter as tk
from socket import gethostname, gethostbyname


class MainPage:
    def __init__(self, server, client):
        self.server = server
        self.client = client

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("Chatting Room")

        width = 600
        height = 500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(geometry)

        self.root.resizable(width=False, height=False)

        # 创建聊天记录框
        self.chat_log = tk.Text(self.root, bd=1, height=20, width=50)
        self.chat_log.config(state=tk.DISABLED)

        # # 创建滚动条
        # self.scrollbar = tk.Scrollbar(self.root, command=self.chat_log.yview)
        # self.chat_log['yscrollcommand'] = self.scrollbar.set

        # 创建文本输入框
        self.entry_field = tk.Text(self.root, bd=1, wrap=tk.WORD)
        self.entry_field.bind("<Return>", lambda event: self.send_message())

        # 创建发送按钮
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)

        # 创建开启服务端按钮
        self.server_button = tk.Button(self.root, text="Enable", takefocus=False)
        # 创建连接按钮
        self.connet_button = tk.Button(self.root, text="Connect", command=self.connect_server)

        # 创建关闭服务端按钮
        self.close_server_button = tk.Button(self.root, text="Close", command=self.server.close)

        # 创建连接按钮
        self.close_client_button = tk.Button(self.root, text="Close", command=self.client.close)

        # 创建服务端ip地址
        self.server_field = tk.Entry(self.root, bd=1)
        self.server_port_field = tk.Entry(self.root, bd=1)
        
        # 创建接收端ip地址
        self.client_field = tk.Entry(self.root, bd=1)
        self.client_port_field = tk.Entry(self.root, bd=1)

        # 设置布局
        # self.scrollbar.grid(row=0, column=3, rowspan=2)
        self.chat_log.place(x=167, y=10, width=426, height=339)
        tk.Label(self.root, text='Message：', anchor="center").grid(row=4, column=2)
        self.entry_field.place(x=167, y=373, width=353, height=100)
        self.send_button.place(x=536, y=372, width=57, height=102)
        tk.Label(self.root, text='Server IP：', anchor="center").place(x=20, y=18, width=67, height=30)
        self.server_field.place(x=20, y=49, width=130, height=30)
        tk.Label(self.root, text='Server Port：', anchor="center").place(x=20, y=96, width=76, height=30)
        self.server_port_field.place(x=20, y=126, width=130, height=30)
        self.server_button.place(x=20, y=176, width=66, height=30)
        self.close_server_button.place(x=98, y=176, width=50, height=30)

        self.server_field.insert(0, gethostbyname(gethostname()))

        tk.Label(self.root, text='Client IP：', anchor="center").place(x=20, y=227, width=66, height=30)
        self.client_field.place(x=19, y=260, width=130, height=30)
        tk.Label(self.root, text='Client Port：', anchor="center").place(x=20, y=304, width=75, height=30)
        self.client_port_field.place(x=20, y=334, width=130, height=30)
        self.connet_button.place(x=20, y=383, width=66, height=30)
        self.close_client_button.place(x=98, y=383, width=50, height=30)


    def mainloop(self):
        # 运行主循环
        self.root.mainloop()

    def open_server(self):
        self.server.init(ip=self.server_field.get(), port=self.server_port_field.get())
        self.root.after(3000, self.connectloop)
        # 每隔一段时间模拟接收消息
        self.root.after(3000, self.receive_message)

    def connectloop(self):
        self.server.waitNewClient()
        self.root.after(3000, self.connectloop)

    def connect_server(self):
        self.client.connect(ip=self.client_field.get(), port=self.client_port_field.get())

    def send_message(self):
        msg = self.entry_field.get('0.0', 'end')
        self.entry_field.delete('0.0', tk.END)
        if msg:
            self.client.send_data(msg)
            self._add_message('You: ', msg)

    def receive_message(self):
        received_msg = self.server.listener()
        if received_msg:
            self._add_message('Friend: ', received_msg)
        self.root.after(500, self.receive_message)

    def _add_message(self, prefix, message):
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, prefix + message)
        self.chat_log.config(state=tk.DISABLED)


if __name__ == '__main__':
    root = MainPage()
    root.mainloop()

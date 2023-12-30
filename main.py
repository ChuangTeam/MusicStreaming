from Page import MainPage
from server import Server
from client import Client
# from socket import gethostname, gethostbyname

if __name__ == '__main__':
    ser = Server()
    cli = Client()

    # ip = gethostbyname(gethostname())

    # port = input('端口号：')

    root = MainPage(ser, cli)
    root.mainloop()

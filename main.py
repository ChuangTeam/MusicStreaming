from Page import MainPage
from server import server
from client import client
from socket import gethostname, gethostbyname
if __name__ == '__main__':
    ser = server()
    cli = client()

    # ip = gethostbyname(gethostname())
    #
    # port = input('端口号：')


    root = MainPage(ser, cli)
    root.mainloop()




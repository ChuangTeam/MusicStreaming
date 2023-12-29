from Page import MainPage
from server import server
from client import client

if __name__ == '__main__':
    ser = server()
    cli = client()
    root = MainPage(ser, cli)
    root.mainloop()




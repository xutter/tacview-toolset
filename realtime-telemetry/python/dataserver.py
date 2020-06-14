from socket import *
from threading import Thread
import json


def serverthread(so):
    so.send("")
    so.recv(1024)

    while True:
        so.send("111111")


def recv_msg():
    with socket(AF_INET,SOCK_DGRAM) as so:
        so.bind(("127.0.0.1",15511))
        while True:
            data = so.recv(1024)


if __name__ == "__main__":
    recv_thread = Thread(target=recv_msg)
    recv_thread.start()
    print("start recv thread")
    
    with socket(AF_INET,SOCK_STREAM,IPPROTO_TCP) as so:
        conf_file = open("config.json","r")
        conf = json.load(conf_file)
        print(conf)
        so.bind((conf["serverip"],conf["serverport"]))
        so.listen()
        print("listen")
        while True:
            print("wait for connect")
            ss = so.accept()
            print("accept")
            t = Thread(target=serverthread,args=(ss,))

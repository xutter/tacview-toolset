from socket import *
from threading import Thread
import json
import time

from sys import path
import os
path.append(os.path.abspath('.'))

print(path)

import parseData as UAV

uav = UAV.Kinematics()

def serverthread(ss):
    global uav
    so,addr = ss

    print('give a handshake: ')
    #print(UAV.HandShakeData + "\n")
    #d = "XtraLib.Stream.0\r\nTacview.RealTimeTelemetry.0\rHost username\r"
    so.send(UAV.HandShakeData1.encode('utf-8'))
    so.send(UAV.HandShakeData2.encode('utf-8'))
    so.send(UAV.HandShakeData3.encode('utf-8'))
    so.send(b'\x00')
    #so.send(d.encode('utf-8'))

    data = so.recv(1024)
    #print('wait for handshake: ')
    #print(data)

    t = time.strftime(UAV.TelReferenceTimeFormat).encode('utf-8')
    
    tt = time.time()
    so.send(UAV.TelFileHeader.encode('utf-8'))
    so.send(t)
    
    while True:
        time.sleep(0.1)
        delta_t = time.time() - tt
        data = uav.pack(delta_t)
        # print(data)
        so.send(data)


def recv_msg():
    global uav
    print("recv uav data start")
    with socket(AF_INET,SOCK_DGRAM) as so:
        so.bind((UAV.LOCALIP,UAV.LOCALPORT))
        #print(UAV.LOCALIP,UAV.LOCALPORT)
        while True:
            data = so.recv(1024)
            uav.parse(data)

if __name__ == "__main__":
    recv_thread = Thread(target=recv_msg)
    recv_thread.start()
    print("start recv thread")
    th = []
    
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
            print("a client connected")
            th.append(Thread(target=serverthread,args=(ss,)))
            print(th)
            th[-1].start()

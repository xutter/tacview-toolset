from socket import *
f = open("data.txt",'w')

with socket(AF_INET,SOCK_STREAM) as so:
    so.bind(('127.0.0.1',33367))
    so.connect(('127.0.0.1',15501))
    so.send(b'    ')
    so.recv(1024)
    try:
        while True:
            data = so.recv(1024)
            f.write(data.decode('utf-8'))
    except:
        print('end')
        f.close()

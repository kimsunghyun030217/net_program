from socket import *
import random
import time

BUFFSIZE = 1024
port = 7000
s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', port))
data, addr = socket.recvfrom(BUFFSIZE)

while True:
    client,addr = s.accpet()
    client.send(time.ctime(time.time()).encode())

    if not data:
        break
    else:
        client.send(data)
        client.send(time.ctime(time.time()).encode())
      
    

s_sock.close()

     
from socket import *

server = ('localhost', 3333)
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    if msg == 'q':
        break
    sock.sendto(msg.encode(), server)
    data, addr = sock.recvfrom(BUFFSIZE)
    print('<- ', data.decode())

sock.close()

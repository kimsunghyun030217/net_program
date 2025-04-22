# client_udp.py
import socket
import time

BUFFSIZE = 1024
client_addr = ('localhost', 9999)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Enter a message( 1 or 2 or 3): ')    
    sock.sendto(msg.encode(),('localhost', 9999))  

    response, addr = sock.recvfrom(BUFFSIZE)      
    print('Server says: ', response.decode())  

sock.close()


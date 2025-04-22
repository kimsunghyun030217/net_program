from socket import *
import time

port = 4321
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

for i in range(3):
    time = 1
    msg = input('입력 >> ')


    while True:
        sock.sendto(msg.encode(), ('localhost', port))
        sock.settimeout(time)
        data, addr = sock.recvfrom(BUF_SIZE)
        count = 0

        if msg == 'quit':
            break
        try:
            data = c_sock.recv(BUFF_SIZE)
            count += 1
        except timeout:
            count += 1 
            if count > 2.0:
                print('Packet({}) lost.'.format(i))
                break


        print('[서버 응답]', data.decode())

sock.close()
print("클라이언트 종료")

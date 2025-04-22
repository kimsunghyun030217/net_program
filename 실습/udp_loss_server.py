from socket import *
import random

BUFF_SIZE = 1024
port = 5555

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))

print('Listening...')

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)

    # 30% 확률로 패킷을 "손실" 시킴
    if random.randint(1, 10) <= 3:
        print('Packet from {} lost!'.format(addr))
        continue

    print('Packet is "{}" from {}'.format(data.decode(), addr))

    # 응답 전송
    s_sock.sendto('ack'.encode(), addr)

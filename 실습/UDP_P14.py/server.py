# UDP Chat Server with ACK and 50% ACK drop (udp_loss_chat_server.py)

import socket
import random
import time

PORT = 3333
BUFFSIZE = 1024

# 서버 소켓 생성 및 바인딩
s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_sock.bind(('', PORT))
print('[SERVER] Listening on port', PORT)

while True:
    data, addr = s_sock.recvfrom(BUFFSIZE)
    message = data.decode()

    # 50% 확률로 ack 손실 시뮬레이션
    if random.random() < 0.5:
        print('[SERVER] [ACK DROPPED] for:', message)
        continue

    print('<-', message)
    s_sock.sendto('ack'.encode(), addr)

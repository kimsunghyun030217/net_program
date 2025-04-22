# udp_student_server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9000))
print('[SERVER] UDP 서버 대기 중...')

while True:
    data, addr = s.recvfrom(1024)
    name = data.decode()
    print('Connection from', addr)
    print('Name:', name)

    # 학번 전송
    student_id = 20221309
    s.sendto(student_id.to_bytes(4, byteorder='big'), addr)

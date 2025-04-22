# udp_student_client.py

import socket

server_addr = ('localhost', 9000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 이름 전송
name = 'sunghyun kim'
sock.sendto(name.encode(), server_addr)

# 학번 수신
data, _ = sock.recvfrom(4)
student_id = int.from_bytes(data, byteorder='big')

print('Student ID:', student_id)
sock.close()

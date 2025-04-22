import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

# 이름 전송
name = 'sunghyun kim'
sock.send(name.encode())

# 학번 수신
student_id_bytes = sock.recv(4)
student_id = int.from_bytes(student_id_bytes, byteorder='big')

print('Student ID:', student_id)

sock.close()

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)


msg = sock.recv(1024)
print(msg.decode())  

name = 'sunghyun kim'
sock.send(name.encode())


student_id = 20221309
sock.send(student_id.to_bytes(4, byteorder='big'))

print(student_id)
sock.close()

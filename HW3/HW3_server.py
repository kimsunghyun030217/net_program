import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)
    client.send(b'Hello ' + addr[0].encode())

    name = client.recv(1024).decode()
    print(name)

    student_id_bytes = client.recv(4)
    student_id = int.from_bytes(student_id_bytes, byteorder='big')


    client.close()

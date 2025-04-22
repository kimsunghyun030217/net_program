import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    # 이름 수신
    name = client.recv(1024).decode()
    print('Name:', name)

    # 학번 보내기
    student_id = 20221309
    client.send(student_id.to_bytes(4, byteorder='big'))

    client.close()

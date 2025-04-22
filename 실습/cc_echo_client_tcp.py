import socket
BUFSIZE = 1024
s = socket.create_connection(('localhost', 2500))
while True:
    msg = input("Message to send: ")
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    if not data:
        break
    print("Received message: %s" % data.decode()) #오른쪽 값을 왼쪽의 %s에 넣는다
s.close()
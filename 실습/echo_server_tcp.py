from socket import *
port - 2500
BUFSIZE = 1024
sock = socket(AF_INFT, SOCK_STREAM)
sock.bind(('',port))
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept
print('connected by' , remotehost, remoteport)

while True:
    data = conn.recv(BUFSIZE)
    print("Received message : ", data.encode())
    conn.send(data)

conn.close()
sock.close
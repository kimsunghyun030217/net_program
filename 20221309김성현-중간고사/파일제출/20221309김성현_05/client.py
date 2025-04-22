from socket import *
BUFF_SIZE = 1024
port = 7000

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

while True:
    msg = input("메시지 입력하세요 : ")
    send_time = sock.send(msg.encode())
    send_time = sock.recv(BUFF_SIZE.decode())

    rev_time = sock.recv(msg.decode())
    rev_time = sock.recv(BUFF_SIZE.docode())
    
    result = rev_time - send_time
    print(result)

sock.close()
# TCP Chat Server with ACK (tcp_ack_chat_server.py)
import socket

PORT = 3333
BUFFSIZE = 1024

# TCP 서버 소켓 생성 및 바인딩
s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', PORT))
s_sock.listen(1)
print('[SERVER] TCP 서버 실행 중... 포트:', PORT)

conn, addr = s_sock.accept()
print('[SERVER] 연결됨:', addr)

while True:
    data = conn.recv(BUFFSIZE)
    if not data:
        break
    message = data.decode()
    print('<-', message)
    conn.send(b'ack')

conn.close()
s_sock.close()
print('[SERVER] 서버 종료')

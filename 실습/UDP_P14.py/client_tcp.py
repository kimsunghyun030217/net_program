# TCP Chat Client with ACK check and retransmission (tcp_ack_chat_client.py)
import socket
import time

PORT = 3333
BUFFSIZE = 1024
MAX_RETRIES = 5
TIMEOUT = 2.0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', PORT))
sock.settimeout(TIMEOUT)

print("[CLIENT] TCP 채팅 클라이언트 실행 중 (재전송 포함)")

while True:
    msg = input('-> ')
    if not msg:
        continue

    for retry in range(MAX_RETRIES):
        try:
            tagged_msg = f"{retry} {msg}"
            sock.send(tagged_msg.encode())
            print(f"[CLIENT] 메시지 전송 (시도 {retry})")

            data = sock.recv(BUFFSIZE)
            if data.decode() == 'ack':
                print("<- ack")
                break
        except socket.timeout:
            print("[CLIENT] 타임아웃. 재전송 중...")
    else:
        print("[CLIENT] 전송 실패: 최대 재시도 초과")

sock.close()
print("[CLIENT] 종료")

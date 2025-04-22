# UDP Chat Client with Retransmission and ACK check (udp_loss_chat_client.py)

import socket
import time

PORT = 3333
BUFFSIZE = 1024
MAX_RETRIES = 5
TIMEOUT = 2.0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

print("[CLIENT] UDP 채팅 클라이언트 실행 중 (재전송 포함)")

while True:
    msg = input('-> ')
    if not msg:
        continue

    for retry in range(MAX_RETRIES):
        # 메시지에 재전송 횟수 붙이기
        tagged_msg = f"{retry} {msg}"
        sock.sendto(tagged_msg.encode(), ('localhost', PORT))
        print(f"[CLIENT] 메시지 전송 (시도 {retry})")

        try:
            data, _ = sock.recvfrom(BUFFSIZE)
            if data.decode() == 'ack':
                print("<- ack")
                break
        except socket.timeout:
            print("[CLIENT] 타임아웃. 재전송 중...")
    else:
        print("[CLIENT] 전송 실패: 최대 재시도 초과")

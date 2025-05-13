import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                break
            print(message.decode())
        except:
            break

HOST = 'localhost'
PORT = 2500

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

my_id = input("ID를 입력하세요: ")
sock.send(f"[{my_id}]".encode())

# 수신 스레드 시작
recv_thread = threading.Thread(target=receive_messages, args=(sock,))
recv_thread.daemon = True
recv_thread.start()

# 입력 전송 루프
while True:
    try:
        msg = input()
        if msg.lower() == 'quit':
            sock.close()
            break
        full_msg = f"[{my_id}] {msg}"
        sock.send(full_msg.encode())
    except:
        break

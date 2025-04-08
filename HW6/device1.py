# device1_server.py
import socket
import random

HOST = 'localhost'
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Device 1 서버 시작")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if data == "quit":
                break
            elif data == "Request":
                temp = random.randint(0, 40)
                humid = random.randint(0, 100)
                ilum = random.randint(70, 150)
                response = f"{temp},{humid},{ilum}"
                conn.sendall(response.encode())

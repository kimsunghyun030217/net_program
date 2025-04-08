# device2_server.py
import socket
import random

HOST = 'localhost'
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Device 2 서버 시작")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if data == "quit":
                break
            elif data == "Request":
                heart = random.randint(40, 140)
                steps = random.randint(2000, 6000)
                cal = random.randint(1000, 4000)
                response = f"{heart},{steps},{cal}"
                conn.sendall(response.encode())

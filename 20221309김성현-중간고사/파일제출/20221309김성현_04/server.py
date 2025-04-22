# device1_server_udp.py
import socket
import random

HOST = 'localhost'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print("[Device 1] UDP 서버 시작")

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()
    if msg == "1":
        temp = random.randint(1,51)
        humid = random.randint(0, 0)
        ilum = random.randint(0,0)
        response = f"{temp},{humid},{ilum}"
        s.sendto(response.encode(), addr)
    
    elif msg == "2":
        temp = random.randint(0,0)
        humid = random.randint(1, 101)
        ilum = random.randint(0,0)
        response = f"{temp},{humid},{ilum}"
        s.sendto(response.encode(), addr)

    elif msg == "3":
        temp = random.randint(0,0)
        humid = random.randint(0, 0)
        ilum = random.randint(1,151)
        response = f"{temp},{humid},{ilum}"
        s.sendto(response.encode(), addr)

    else:
        break
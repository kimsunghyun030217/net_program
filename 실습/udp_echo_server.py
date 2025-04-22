import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

print(f"UDP echo server is running on port {port}...")

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    print('Received from', addr, ':', msg.decode())
    sock.sendto(msg, addr)  # 받은 그대로 다시 보냄 (echo)

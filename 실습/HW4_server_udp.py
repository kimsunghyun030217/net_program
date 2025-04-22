# udp_calc_server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9000))
print('[SERVER] UDP 계산 서버 실행 중...')

while True:
    data, addr = s.recvfrom(1024)
    expr = data.decode().strip()

    if not expr:
        continue

    try:
        result = eval(expr)
        if isinstance(result, float):
            result = round(result, 1)
        s.sendto(str(result).encode(), addr)
    except Exception as e:
        s.sendto(f"Error: {str(e)}".encode(), addr)

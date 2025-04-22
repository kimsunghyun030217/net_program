# udp_calc_client.py

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 9000)

while True:
    expr = input("계산식을 입력하세요 (종료는 q): ")
    if expr.lower() == 'q':
        break

    sock.sendto(expr.encode(), server_addr)

    result, _ = sock.recvfrom(1024)
    print("결과:", result.decode())

sock.close()

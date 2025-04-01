import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9000))

while True:
    expr = input("계산식을 입력하세요 : , 종료는 q: ")
    if expr.lower() == 'q':
        break

    sock.send(expr.encode())  

    result = sock.recv(1024).decode()
    print("결과:", result)

sock.close()

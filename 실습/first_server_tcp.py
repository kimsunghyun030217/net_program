import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
        clinet, addr = s.accept()
        print('Connextion from', addr)
        clinet.send(b'Hello' + addr[0].encode())
        clinet.close()
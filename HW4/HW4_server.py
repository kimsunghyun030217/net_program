import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    while True:
        data = client.recv(1024)
        if not data:
            break 

        expr = data.decode().strip()

        try:
    
            result = eval(expr)
            if isinstance(result, float):
                result = round(result, 1)
            client.send(str(result).encode())

        except Exception as e:
            client.send(f"Error: {str(e)}".encode())

    client.close()

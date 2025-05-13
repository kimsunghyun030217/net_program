import socket
import select

HOST = 'localhost'
PORT = 2500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('Server started...')

sockets_list = [server_socket]
clients = {}

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for sock in read_sockets:
        if sock == server_socket:
            client_socket, client_address = server_socket.accept()
            sockets_list.append(client_socket)
            print(f"New connection from {client_address}")
        else:
            try:
                message = sock.recv(1024)
                if not message:
                    sockets_list.remove(sock)
                    sock.close()
                    continue

                # 다른 모든 클라이언트에게 전송
                for client in sockets_list:
                    if client != server_socket and client != sock:
                        client.send(message)

            except:
                sockets_list.remove(sock)
                sock.close()
                continue

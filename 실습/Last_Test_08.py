# proxy_server.py
# 브라우저로부터 HTTP 요청을 받아 실제 웹 서버에 대신 요청하고 응답을 다시 브라우저에 전달하는 프록시 서버 구현

import socket

# 설정 값들
LISTEN_PORT = 9000  # 프록시 서버가 열릴 포트
BUFFER_SIZE = 4096  # 한 번에 받을 최대 데이터 크기
REAL_SERVER_HOST = 'www.daum.net'  # 실제로 요청을 보낼 외부 서버
REAL_SERVER_PORT = 80  # HTTP 기본 포트

# 프록시 서버 소켓 생성 및 바인딩
def start_proxy_server():
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_sock.bind(('', LISTEN_PORT))
    listen_sock.listen(1)
    print(f'[프록시 서버] 포트 {LISTEN_PORT}에서 대기 중...')

    while True:
        client_conn, client_addr = listen_sock.accept()
        print(f'[프록시 서버] 클라이언트 접속: {client_addr}')

        # 클라이언트로부터 HTTP 요청 받기
        request = client_conn.recv(BUFFER_SIZE)
        print(f'[프록시 서버] 수신한 요청:\n{request.decode(errors="ignore")}')

        # 외부 서버 소켓 생성 및 연결
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as remote_sock:
            remote_sock.connect((REAL_SERVER_HOST, REAL_SERVER_PORT))
            remote_sock.sendall(request)  # 외부 서버로 원본 요청 전송

            # 외부 서버로부터 응답 수신 및 클라이언트로 전달
            while True:
                response = remote_sock.recv(BUFFER_SIZE)
                if not response:
                    break
                client_conn.sendall(response)

        client_conn.close()
        print('[프록시 서버] 클라이언트 연결 종료\n')

if __name__ == '__main__':
    start_proxy_server()

from socket import *
import os

# 포트 번호 (IIS 끈 경우 80, 아니면 8080 사용)
PORT = 80

# 웹서버 소켓 생성
s = socket()
s.bind(('', PORT))
s.listen(10)
print(f'웹서버 실행 중... (http://127.0.0.1:{PORT}/index.html)')

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    
    if not msg:
        c.close()
        continue

    # 요청 라인 파싱
    request_line = msg.split('\r\n')[0] #HTTP 요청 메시지의 첫 줄 파싱
    print('요청 라인:', request_line)

    try:
        filename = request_line.split()[1][1:]  # GET /index.html HTTP/1.1 같은 요청에서 'index.html'만 추출하는 코드
    except IndexError:
        c.close()
        continue

    # 빈 요청일 경우 index.html
    if filename == '':
        filename = 'index.html'

    # 파일이 존재하는 경우
    if os.path.exists(filename):
        # MIME 타입 결정
        if filename.endswith('.html'):
            mimeType = 'text/html'
            f = open(filename, 'r', encoding='utf-8')
            data = f.read()
            c.send(('HTTP/1.1 200 OK\r\n').encode())
            c.send((f'Content-Type: {mimeType}\r\n').encode())
            c.send(('\r\n').encode())
            c.send(data.encode('euc-kr'))  
            f.close()

        elif filename.endswith('.ico'):
            mimeType = 'image/x-icon'
            f = open(filename, 'rb')
            data = f.read()
            c.send(('HTTP/1.1 200 OK\r\n').encode())
            c.send((f'Content-Type: {mimeType}\r\n').encode())
            c.send(('\r\n').encode())
            c.send(data)
            f.close()

        elif filename.endswith('.png'):
            mimeType = 'image/png'
            f = open(filename, 'rb')
            data = f.read()
            c.send(('HTTP/1.1 200 OK\r\n').encode())
            c.send((f'Content-Type: {mimeType}\r\n').encode())
            c.send(('\r\n').encode())
            c.send(data)
            f.close()

        else:
            c.send(('HTTP/1.1 404 Not Found\r\n\r\n').encode())
            c.send(('<html><body>Not Found</body></html>').encode('euc-kr'))
    else:
        c.send(('HTTP/1.1 404 Not Found\r\n\r\n').encode())
        c.send(('<html><body>Not Found</body></html>').encode('euc-kr'))

    c.close()

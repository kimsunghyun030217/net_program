from socket import *
import random

BUF_SIZE = 1024
port = 4321

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('[SERVER] Listening on port', port)

mbox = {}  # mboxID별로 메시지 저장하는 딕셔너리

while True:
    data, addr = s_sock.recvfrom(BUF_SIZE)
    if random.randint(1,10) <= 0.25:
        continue
    s_sock.sendto('ack'.encode,addr)
    
    
    msg = data.decode()
    if msg == 'quit':
        print('[SERVER] 종료 요청 받음')
        break

    elif msg.startswith('send'):  #startswith()는 파이썬에서 문자열이 특정 문자열로 시작하는지 확인하는 함수
        _, mboxid, *message = msg.split()  #첫 번째 단어는 send여서 무시해도 됨 , 두 번째 단어는 메일박스 이름, 세 번째 단어는 나머지 전부
        message = ' '.join(message)

        if mboxid not in mbox:
            mbox[mboxid] = []

        mbox[mboxid].append(message)
        s_sock.sendto(b"OK", addr)

    elif msg.startswith('receive'):
        _, mboxid = msg.split()  #꺼내고 싶은 메일박스

        if mboxid in mbox and mbox[mboxid]: #mboxid라는 키가 mbox 딕셔너리에 존재하는지, mbox[mboxid]가 비어 있지 않은지
            rep = mbox[mboxid].pop(0) # 리스트 맨 앞 요소를 꺼내서 제거함
            s_sock.sendto(rep.encode(), addr)
        else:
            s_sock.sendto(b'No messages', addr)

s_sock.close()
print('[SERVER] 종료됨')

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

        expr = data.decode().strip() #받은 데이터 문자열 변환 + .strip() : 앞 뒤 공백 제거

        try:
    
            result = eval(expr)
            if isinstance(result, float):  #실수 결과일 경우 소수 첫째 자리까지 반올림
                #isinstance()는 파이썬에서 **"이 객체가 이 타입(자료형)이 맞는지 확인"**할 때 사용하는 함수
                result = round(result, 1)
            client.send(str(result).encode())

        except Exception as e:
            client.send(f"Error: {str(e)}".encode())

    client.close()

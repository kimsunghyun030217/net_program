# DNS 클라이언트 프로그램 (dns_client.py)
# 주어진 도메인 이름에 대해 DNS 쿼리를 생성하고, 응답으로부터 IP 주소를 추출함

import socket
import struct
import sys

class DnsClient:
    def __init__(self, domainName):
        self.domainName = domainName
        # DNS Query Header
        self.TransactionId = 1
        self.Flag = 0x0100         # 일반적인 쿼리 요청 (Recursion Desired)
        self.Questions = 1         # 질문 하나
        self.AnswerRRs = 0
        self.AuthorityRRs = 0
        self.AdditionalRRs = 0

    def response(self, packet):
        # 수신된 DNS 응답 패킷에서 IP 주소를 추출
        dnsHeader = packet[:12]  # DNS 응답 헤더는 항상 12바이트
        dnsData = packet[12:].split(b'\x00', 1)  # 질문 끝 위치 찾기
        ansRR = packet[12 + len(dnsData[0]) + 5 : 12 + len(dnsData[0]) + 21]  # 응답 영역 추출

        # 응답 리소스 레코드 파싱 (TYPE, CLASS, TTL, 데이터 길이, IP 주소)
        rr_unpack = struct.unpack('!2sHHIH4s', ansRR)
        ip_addr = socket.inet_ntoa(rr_unpack[5])
        print(self.domainName, ip_addr)

    def query(self):
        # DNS 쿼리 메시지 생성
        query = struct.pack('!HH', self.TransactionId, self.Flag)
        query += struct.pack('!HH', self.Questions, self.AnswerRRs)
        query += struct.pack('!HH', self.AuthorityRRs, self.AdditionalRRs)

        # 도메인 이름을 QNAME 포맷으로 변환 (길이 + 문자열 + ... + 0x00)
        part = self.domainName.split('.')
        for label in part:
            query += struct.pack('!B', len(label))
            query += label.encode()
        query += b'\x00'  # 도메인 이름 끝 표시

        query_type = 1  # Type A (IPv4)
        query_class = 1  # Class IN (인터넷)
        query += struct.pack('!HH', query_type, query_class)

        # 소켓 생성 및 DNS 서버로 전송
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = ('8.8.8.8', 53)  # 구글 public DNS 서버 주소
        sock.sendto(query, addr)

        # 응답 수신 후 처리
        packet, _ = sock.recvfrom(65535)
        self.response(packet)

# 명령행 인자로 도메인 이름을 받아 실행
if __name__ == '__main__':
    if len(sys.argv) > 1:
        client = DnsClient(sys.argv[1])
        client.query()

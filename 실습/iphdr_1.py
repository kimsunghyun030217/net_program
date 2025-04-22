import socket
import struct
import binascii

class Iphdr:
    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45         # IPv4 + 헤더 길이(5*4=20 bytes)
        self.tos = 0                # Type of Service
        self.tot_len = tot_len      # 전체 패킷 길이
        self.id = 0                 # ID
        self.frag_off = 0           # Fragment offset
        self.ttl = 127              # Time To Live
        self.protocol = protocol    # TCP(6) or UDP(17)
        self.check = 0              # Checksum (임시로 0)
        self.saddr = socket.inet_aton(saddr)  # Source IP
        self.daddr = socket.inet_aton(daddr)  # Destination IP
def pack_Iphdr(self):
    packed = b''
    packed += struct.pack('!BBH', self.ver_len, self.tos, self.tot_len) #struct.pack()은 데이터를 바이트(binary) 형식으로 변환
    packed += struct.pack('!HH', self.id, self.frag_off)
    packed += struct.pack('!BBH', self.ttl, self.protocol, self.check)
    packed += struct.pack('!4s', self.saddr)
    packed += struct.pack('!4s', self.daddr)
    return packed


ip = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')  #1000: 패킷 총 길이,6: TCP 프로토콜
packed_iphdr = ip.pack_Iphdr() #IP 주소는 inet_aton()으로 바이너리 4바이트로 변환됨
print(binascii.b2a_hex(packed_iphdr)) #binascii.b2a_hex() → 바이트 → 16진수 문자열로 보기 쉽게 출력
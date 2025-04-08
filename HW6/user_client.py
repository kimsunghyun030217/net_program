# client.py
import socket
import time

def get_time_string():
    return time.ctime(time.time())

def log_data(device_id, data):
    with open("data.txt", "a") as f:
        timestamp = get_time_string()
        if device_id == 1:
            temp, humid, ilum = data.split(",")
            f.write(f"{timestamp}: Device1: Temp={temp}, Humid={humid}, Iilum={ilum}\n")
        else:
            heart, steps, cal = data.split(",")
            f.write(f"{timestamp}: Device2: Heartbeat={heart}, Steps={steps}, Cal={cal}\n")

def main():
    device1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    device2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    device1.connect(('localhost', 9001))
    device2.connect(('localhost', 9002))

    count1 = count2 = 0

    while True:
        cmd = input("Enter 1 (Device1), 2 (Device2), or quit: ")
        if cmd == '1':
            device1.sendall(b"Request")
            data = device1.recv(1024).decode()
            log_data(1, data)
            count1 += 1
        elif cmd == '2':
            device2.sendall(b"Request")
            data = device2.recv(1024).decode()
            log_data(2, data)
            count2 += 1
        elif cmd == 'quit':
            device1.sendall(b"quit")
            device2.sendall(b"quit")
            break
        else:
            print("Invalid command")

    device1.close()
    device2.close()

    print(f"종료됨. 수집 결과 - Device1: {count1}개, Device2: {count2}개")

if __name__ == "__main__":
    main()

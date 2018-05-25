#!/usr/bin/env python3
#	encoding:utf-8
#	CLIENT

import sys
import socket
from socket import *

HOST = '192.168.81.88'
PORT = 55555
addr = (HOST, PORT)

#一次接收这么多bytes
BUFFERSIZE = 1024

# SOCK_DGRAM ：UDP数据报
s = socket(AF_INET, SOCK_DGRAM)
# socket类s去连接服务器
s.connect((HOST, PORT))

def client_print(*msg):
    print("CLIENT: ", msg)

while True:
    kel = input('Question >>')
    if kel == 'exit':
        break

    client_print('input data: %s' % kel)
    # python3 socket 只能收发二进制数据，需要转码
    kel = kel.encode(encoding='utf-8')
    #s.sendall(kel)
    # 发送数据
    try:
        s.sendto(kel, addr)
        # 接收数据
        data, addr = s.recvfrom(BUFFERSIZE)
        client_print("recived message from server({0}:{1}) : {2}".format(addr[0], addr[1], data.decode('utf-8')))
    except ConnectionRefusedError:
        client_print("exit client")
        s.close()

if not s._closed:
    s.close()

sys.exit()

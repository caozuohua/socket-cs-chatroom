#!/usr/bin/env python3
#	encoding:utf-8
#	CLIENT

import sys
import socket
from socket import *

HOST = '192.168.81.88'
PORT = 55555
addr = (HOST, PORT)

#只接收这么多bytes
buffersize = 10

s = socket(AF_INET, SOCK_DGRAM)
# socket类s去连接服务器
s.connect((HOST, PORT))

while True:
    kel = input('Question :>>')
    #if kel == 'exit':
    #    break
    # python3 socket 只能收发二进制数据，需要转码
    kel = kel.encode(encoding='utf-8')
    print('input data: %r' % kel)
    #s.sendall(kel)
    # 发送数据
    s.sendto(kel, addr)
    #TODO: 目前客户端无法即使正常退出
    #if kel == 'exit':
    #    print('BYE! ')
    #    break
    # 接收数据
    data, addr = s.recvfrom(buffersize)
    print(data.decode(encoding='utf-8'), 'from', addr)

s.close()
sys.exit()

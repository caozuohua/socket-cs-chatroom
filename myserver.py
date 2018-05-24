#!/usr/bin/env python3
#	encoding:utf-8
#
#	SERVER
#

import socket
from socket import *
import time

HOST = '192.168.81.88'
PORT = 55555

#只接收这么多个bytes
buffersize = 10

# socket类
s = socket(AF_INET, SOCK_DGRAM)
# s绑定主机地址和端口
s.bind((HOST, PORT))
#s.listen(10)


#简单地监听客户端的消息，收到消息后回复确认
while True:
    print("=== THE SERVER START WORKING ===")
   # 此处的s.recvfrom方法和s.recv都会返回接收到的数据，而recvfrom还会返回客户端的地址
    data, addr = s.recvfrom(buffersize)
    data = data.decode(encoding='utf-8')
   # 目前服务端和客户端无法一起结束运行
   # if data == 'exit':
   #     print('SERVER EXITED!')
   #     s.sendto("SERVER EXITED! ".encode(encoding='utf-8'), addr)
   #     time.sleep(5)
   #     break
    print("recived data: %s" % data)
    with open('dialog.log', 'a') as logfile:
        logfile.write(data + '\n')

   # 回复消息
    s.sendto("SERVER recived ".encode(encoding='utf-8'), addr)
s.close()

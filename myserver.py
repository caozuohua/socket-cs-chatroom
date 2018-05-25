#!/usr/bin/env python3
# encoding:utf-8
#
#	SERVER
#

import socket
from socket import *
import os

HOST = '192.168.81.88'
PORT = 55555

#只接收这么多个bytes
BUFFERSIZE = 1024

# socket实例，TCP连接 
s = socket(AF_INET, SOCK_DGRAM)
# 重用ip和端口
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# s绑定主机地址和端口
s.bind((HOST, PORT))
# 监听队列
#s.listen()
# 服务器对话日志
logfile = 'dialog.log'

def server_print(*msg):
    print("SERVER: ", msg)

def clean_up():
    if os.path.exists(logfile):
        os.remove(logfile)

clean_up()

# 简单地监听客户端的消息，收到消息后回复确认
while True:
    print("=== THE SERVER START WORKING ===")
   # 此处的s.recvfrom方法和s.recv都会返回接收到的数据，而recvfrom还会返回客户端的地址
    data, addr = s.recvfrom(BUFFERSIZE)
    data = data.decode(encoding='utf-8')
    server_print("recived message from client(%s): %s" % (addr, data))
    with open(logfile, 'a') as f:
        log = "client{0} \t message: {1}\n".format(addr, data)
        f.write(log)

   
   # 回复消息
    s.sendto("SERVER ROGER THAT ".encode(encoding='utf-8'), addr)

if not s._closed():
    s.close()


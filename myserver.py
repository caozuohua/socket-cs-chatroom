#!/usr/bin/env python3
# encoding:utf-8
#
#	SERVER
#

import socket
from socket import *
import os

class ServerAddr():
    HOST = '192.168.81.88'
    PORT = 55555
    BUFFERSIZE = 1024
    logfile = 'dialog.log'

def start_udp_server():
    host = ServerAddr()
    ip_port = (host.HOST, host.PORT)
    # UDP socket
    s = socket(AF_INET, SOCK_DGRAM)
    # 重用ip和端口
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ip_port)
    # 监听队列
    #s.listen(5)
    
    def _server_print(*msg):
        print("SERVER: %s" % msg)
    
    def _clean_up():
        if os.path.exists(host.logfile):
            os.remove(host.logfile)
    
    _clean_up()
    
    # 简单地监听客户端的消息，收到消息后回复确认
    while True:
        _server_print("=== THE SERVER START WORKING ===")
       # 此处的s.recvfrom方法和s.recv都会返回接收到的数据，而recvfrom还会返回客户端的地址
        data, addr = s.recvfrom(host.BUFFERSIZE)
        data = data.decode(encoding='utf-8')
        _server_print("recived message from client(%s): %s" % (addr, data))
        with open(host.logfile, 'a') as f:
            log = "client{0} \t message: {1}\n".format(addr, data)
            f.write(log)
    
       
       # 回复消息
        s.sendto("SERVER ROGER THAT".encode(encoding='utf-8'), addr)
    
    if not s._closed():
        s.close()

if __name__ == '__main__':
    start_udp_server()

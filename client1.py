#!/usr/bin/env python3
#	encoding:utf-8
#	CLIENT

import sys
import socket
from socket import *

class ServerAddr():
    HOST = '192.168.81.88'
    PORT = 55555
    BUFFERSIZE = 1024

def start_udp_client():
    host = ServerAddr()
    # SOCK_DGRAM : UDP socket 
    s = socket(AF_INET, SOCK_DGRAM)
    ip_port = (host.HOST, host.PORT)
    s.connect(ip_port)
    
    def client_print(*msg):
        print("CLIENT: %s" % msg)
    
    while True:
        kel = input('Question >>')
        if kel == 'exit':
            break
    
        client_print('input data: %s' % kel)
        # python3 socket 只能收发二进制数据，需要转码
        kel = kel.encode(encoding='utf-8')
        try:
            # s.sendall(kel)
            s.sendto(kel, ip_port)
            # 接收数据
            data, addr = s.recvfrom(host.BUFFERSIZE)
            client_print("recived message from server({0}:{1}) : {2}".format(addr[0], addr[1], data.decode('utf-8')))
        except ConnectionRefusedError:
            client_print("exit client")
            s.close()
    
    if not s._closed:
        s.close()
    
if __name__ == '__main__':
    start_udp_client()
    sys.exit()

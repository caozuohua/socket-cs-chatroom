#!/usr/bin/env python3
# encoding:utf-8

import socket, select

class Chat_server():
    def __init__(self):
        self.CONNECTION_LIST = []
        self.RECV_BUFFER = 4096
        self.PORT = 55555
        self.LOCAL_ADDR = '192.168.81.86'
        self.server_socket = None
        self.read_sockets, write_sockets, error_sockets = select.select(self.CONNECTION_LIST, [], [])

    def broadcast_data(self, sock, message):
        for socket in self.CONNECTION_LIST:
            if socket not in (self.server_socket, sock):
                try:
                    socket.send(message)
                except:
                    socket.close()
                    self.CONNECTION_LIST.remove(socket)

    def start_server(self):
        # TCP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("self.server_socket: %s" % self.server_socket)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.LOCAL_ADDR, self.PORT))
        # self.server_socket.listen(10)
        print("ok")
        self.CONNECTION_LIST.append(self.server_socket)

        addr = None

        print("SERVER starts on localhost:", self.PORT)

        while True:
            # read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST,[],[])

            for sock in self.read_sockets:
                if sock == self.server_socket:
                    sockfd, addr = self.server_socket.accept()
                    self.CONNECTION_LIST.append(sockfd)
                    print("CLIENT %s connected" % addr)
                else:
                    try:
                        data = sock.recv(self.RECV_BUFFER)
                        if data:
                            self.broadcast_data(sock, data)
                    except:
                        self.broadcast_data(sock, "Client %s is offline" % addr)
                    print("Client %s is offline" % addr)
                    sock.close()
                    self.CONNECTION_LIST.remove(sock)
                    continue
        if not server_socket.closed:
            server_socket.close()


if __name__ == '__main__':
    c_s = Chat_server()
    c_s.start_server()


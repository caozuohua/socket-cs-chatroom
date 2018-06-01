#!/usr/bin/env python3
# encoding:utf-8

import socket, select

class Chat_server():
    def __init__(self):
        self.CONNECTION_LIST = []
        self.RECV_BUFFER = 4096
        self.PORT = 55555
        self.LOCAL_ADDR = '192.168.81.86'

    def broadcast_data(self, server_socket, sock, message):
        for socket in self.CONNECTION_LIST:
            if socket not in (server_socket, sock):
                try:
                    socket.send(message)
                except:
                    socket.close()
                    self.CONNECTION_LIST.remove(socket)

    def start_server(self):
        # TCP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.LOCAL_ADDR, self.PORT))
        # work with socket.accept()
        server_socket.listen(10)
        self.CONNECTION_LIST.append(server_socket)

        print("SERVER starts:", self.LOCAL_ADDR, self.PORT)

        while True:
            read_sockets, write_sockets, error_sockets = select.select(self.CONNECTION_LIST,[],[])

            for sock in read_sockets:
                if sock == server_socket:
                    sockfd, addr = server_socket.accept()
                    self.CONNECTION_LIST.append(sockfd)
                    print("CLIENT connected", addr)
                else:
                    try:
                        data = sock.recv(self.RECV_BUFFER)
                        if data:
                            self.broadcast_data(server_socket, sock, data)
                    except OSError:
                        # FIXME: this seems to will never be triggered
                        self.broadcast_data(sock, server_socket, "Client {0} is offline".format(addr))
                        print("Client is offline", addr)
                        sock.close()
                        # self.CONNECTION_LIST.remove(sock)
                        continue
        if not server_socket.closed:
            server_socket.close()


if __name__ == '__main__':
    c_s = Chat_server()
    c_s.start_server()


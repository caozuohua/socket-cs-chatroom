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
        '''
        :param server_socket: socket of the chat server
        :param sock: socket received from clients
        :param message: message to send to clients
        :return: don`t return
        '''
        for socket in self.CONNECTION_LIST:
            if socket not in (server_socket, sock):
                try:
                    message = "<{0}:{1}> {2}".format(sock.getpeername()[0], sock.getpeername()[1], message)
                    print(message)
                    socket.send(message.encode('utf-8'))
                except :
                    print("broadcast_data error")

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
            read_sockets, write_sockets, error_sockets = select.select(self.CONNECTION_LIST, [], [])

            for sock in read_sockets:
                if sock == server_socket:
                    sockfd, addr = server_socket.accept()
                    self.CONNECTION_LIST.append(sockfd)
                    print("CLIENT connected", addr)
                else:
                    try:
                        data = sock.recv(self.RECV_BUFFER).decode('utf-8')
                        if data:
                            self.broadcast_data(server_socket, sock, data)
                        else:
                            self.CONNECTION_LIST.remove(sock)
                            # broadcast to all online clients that someone is offline
                            self.broadcast_data(server_socket, sock, "Client {0} is offline".format(sock.getpeername()))
                            print("Client is offline:")
                            if not sock._closed:
                                print("sock closed now")
                                sock.close()
                            continue
                    except OSError:
                        # self.broadcast_data(sock, server_socket, "Client {0} is offline".format(addr))
                        print("Client is offline")
                        print("sock: ", sock)
                        sock.close()
                        continue
        if not server_socket.closed:
            server_socket.close()


if __name__ == '__main__':
    c_s = Chat_server()
    c_s.start_server()


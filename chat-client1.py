#!/usr/bin/env python3
# encoding:utf-8

import socket, select, sys

class Chat_client():
    def __init__(self):
        self.host = '192.168.81.86'
        self.port = 55555
        self.s = None
        self.RECV_BUFFER = 4096

    def prompt(self):
        sys.stdout.write('<YOU> ')
        sys.stdout.flush()

    def start_client(self):

        # if (len(sys.argv) < 3):
        #     print("Usage: python3 {0} hostname port".format(sys.argv[0]))
        #     sys.exit()
        # host = sys.argv[1]
        # port = int(sys.argv[2])

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        try:
            s.connect((self.host, self.port))
        except OSError:
            print('connection failed! ')
            sys.exit()

        print('connection succeed! ')
        self.prompt()

        while True:
            socket_list = [sys.stdin, ]

            read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

            for sock in read_sockets:
                if sock == s:
                    data = sock.recv(self.RECV_BUFFER)
                    if not data:
                        print("\n Disconnected from chat server")
                        # sys.exit()
                        continue
                    else:
                        # bytes decode to str
                        sys.stdout.write(data.decode('utf-8'))
                        self.prompt()
                else:
                    msg = sys.stdin.readline().strip()
                    # print('===' + msg)
                    # str encode to bytes
                    s.send(msg.encode('utf-8'))
                    self.prompt()
        if not s.closed:
            s.close()


if __name__ == '__main__':
    c_c = Chat_client()
    c_c.start_client()
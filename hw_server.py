import socketserver

import struct
from time import ctime

HOST = ''
PORT = 22222
BUFSIZ = 2222
ADDR = (HOST, PORT)

class myRH(socketserver.StreamRequestHandler):
    def handle(self):
        connect = self.request
        print('connected from', self.client_address)
        while True:

            try:



                #data = str(connect.recv(BUFSIZ), 'utf-8')
                data = self.rfile.readline().strip()
                print (struct.unpack(data))
                break
                print ('read!')
                #self.wfile.write(bytes(ctime() + data, 'utf-8'))
                self.wfile.write(bytes(ctime(), 'utf-8'))
                self.wfile.write(data)
                print ('write!')
            except:
                break
tcpServ = socketserver.ThreadingTCPServer(ADDR, myRH)
tcpServ.serve_forever()


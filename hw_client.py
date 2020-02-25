from socket import *
import struct
from time import ctime


HOST = '127.0.0.1'
PORT = 22222
BUFSIZ = 2222
ADDR = (HOST, PORT)



while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    #data = input('>')
    data = 2154
    if not data:
        break

    tcpCliSock.sendall(struct.pack(data))
    break
    tcpCliSock.sendall(bytes(data + '\n','utf-8'))
    tcpCliSock.sendall(bytes(data+ '\n', 'utf-8'))
    tcpCliSock.sendall(bytes(data+ '\n', 'utf-8'))
    print ('send!')
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        print('received')
        if not data:
            break

        print (str(data, 'utf-8'))

    tcpCliSock.close()
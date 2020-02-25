from PyQt5 import QtCore, QtGui, QtWidgets

from windows import window_login

import socket

import MySQLdb





if __name__ == "__main__":
    import sys


    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    app = QtWidgets.QApplication(sys.argv)
    wd_login = window_login()
    wd_login.show()

    #wd_register = window_register()
    #wd_register.show()


    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_login(object):
    def setupUi(self, form_login):
        form_login.setObjectName("form_login")
        form_login.resize(492, 404)
        self.pushButton_login = QtWidgets.QPushButton(form_login)
        self.pushButton_login.setGeometry(QtCore.QRect(190, 290, 93, 28))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_register = QtWidgets.QPushButton(form_login)
        self.pushButton_register.setGeometry(QtCore.QRect(10, 30, 93, 28))
        self.pushButton_register.setObjectName("pushButton_register")
        self.label_account = QtWidgets.QLabel(form_login)
        self.label_account.setGeometry(QtCore.QRect(60, 150, 55, 16))
        self.label_account.setObjectName("label_account")
        self.label_password = QtWidgets.QLabel(form_login)
        self.label_password.setGeometry(QtCore.QRect(60, 220, 55, 16))
        self.label_password.setObjectName("label_password")
        self.plainTextEdit_account = QtWidgets.QPlainTextEdit(form_login)
        self.plainTextEdit_account.setGeometry(QtCore.QRect(170, 140, 161, 31))
        self.plainTextEdit_account.setObjectName("plainTextEdit_account")
        self.plainTextEdit_password = QtWidgets.QPlainTextEdit(form_login)
        self.plainTextEdit_password.setGeometry(QtCore.QRect(170, 210, 161, 31))
        self.plainTextEdit_password.setObjectName("plainTextEdit_password")

        self.retranslateUi(form_login)
        self.pushButton_register.clicked.connect(form_login.showRegister)
        QtCore.QMetaObject.connectSlotsByName(form_login)

    def retranslateUi(self, form_login):
        _translate = QtCore.QCoreApplication.translate
        form_login.setWindowTitle(_translate("form_login", "Form"))
        self.pushButton_login.setText(_translate("form_login", "Login"))
        self.pushButton_register.setText(_translate("form_login", "Register"))
        self.label_account.setText(_translate("form_login", "Account"))
        self.label_password.setText(_translate("form_login", "Password"))


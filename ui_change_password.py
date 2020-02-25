# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_password.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_change_password(object):
    def setupUi(self, form_change_password):
        form_change_password.setObjectName("form_change_password")
        form_change_password.resize(400, 300)
        self.label_oldPassword = QtWidgets.QLabel(form_change_password)
        self.label_oldPassword.setGeometry(QtCore.QRect(30, 30, 101, 41))
        self.label_oldPassword.setObjectName("label_oldPassword")
        self.label_newPassword = QtWidgets.QLabel(form_change_password)
        self.label_newPassword.setGeometry(QtCore.QRect(30, 100, 101, 41))
        self.label_newPassword.setObjectName("label_newPassword")
        self.plainTextEdit_oldPassword = QtWidgets.QPlainTextEdit(form_change_password)
        self.plainTextEdit_oldPassword.setGeometry(QtCore.QRect(200, 40, 161, 31))
        self.plainTextEdit_oldPassword.setObjectName("plainTextEdit_oldPassword")
        self.plainTextEdit_newPassword = QtWidgets.QPlainTextEdit(form_change_password)
        self.plainTextEdit_newPassword.setGeometry(QtCore.QRect(200, 110, 161, 31))
        self.plainTextEdit_newPassword.setObjectName("plainTextEdit_newPassword")
        self.pushButton_change_password = QtWidgets.QPushButton(form_change_password)
        self.pushButton_change_password.setGeometry(QtCore.QRect(140, 220, 93, 28))
        self.pushButton_change_password.setObjectName("pushButton_change_password")

        self.retranslateUi(form_change_password)
        self.pushButton_change_password.clicked.connect(form_change_password.change_password)
        QtCore.QMetaObject.connectSlotsByName(form_change_password)

    def retranslateUi(self, form_change_password):
        _translate = QtCore.QCoreApplication.translate
        form_change_password.setWindowTitle(_translate("form_change_password", "Form"))
        self.label_oldPassword.setText(_translate("form_change_password", "Old Password"))
        self.label_newPassword.setText(_translate("form_change_password", "New Password"))
        self.pushButton_change_password.setText(_translate("form_change_password", "Submit"))


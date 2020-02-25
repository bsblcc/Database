# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_register(object):
    def setupUi(self, form_register):
        form_register.setObjectName("form_register")
        form_register.resize(514, 438)
        self.label_account = QtWidgets.QLabel(form_register)
        self.label_account.setGeometry(QtCore.QRect(30, 50, 55, 16))
        self.label_account.setObjectName("label_account")
        self.label_password_input = QtWidgets.QLabel(form_register)
        self.label_password_input.setGeometry(QtCore.QRect(20, 110, 131, 51))
        self.label_password_input.setObjectName("label_password_input")
        self.label_password_varify = QtWidgets.QLabel(form_register)
        self.label_password_varify.setGeometry(QtCore.QRect(10, 210, 171, 21))
        self.label_password_varify.setObjectName("label_password_varify")
        self.plainTextEdit_account = QtWidgets.QPlainTextEdit(form_register)
        self.plainTextEdit_account.setGeometry(QtCore.QRect(180, 50, 161, 31))
        self.plainTextEdit_account.setObjectName("plainTextEdit_account")
        self.plainTextEdit_password_input = QtWidgets.QPlainTextEdit(form_register)
        self.plainTextEdit_password_input.setGeometry(QtCore.QRect(180, 120, 171, 31))
        self.plainTextEdit_password_input.setObjectName("plainTextEdit_password_input")
        self.plainTextEdit_password_varify = QtWidgets.QPlainTextEdit(form_register)
        self.plainTextEdit_password_varify.setGeometry(QtCore.QRect(180, 210, 178, 31))
        self.plainTextEdit_password_varify.setObjectName("plainTextEdit_password_varify")
        self.label_phoneNumber = QtWidgets.QLabel(form_register)
        self.label_phoneNumber.setGeometry(QtCore.QRect(20, 310, 101, 31))
        self.label_phoneNumber.setObjectName("label_phoneNumber")
        self.label_sex = QtWidgets.QLabel(form_register)
        self.label_sex.setGeometry(QtCore.QRect(40, 380, 61, 41))
        self.label_sex.setObjectName("label_sex")
        self.comboBox_sex = QtWidgets.QComboBox(form_register)
        self.comboBox_sex.setGeometry(QtCore.QRect(200, 400, 73, 22))
        self.comboBox_sex.setObjectName("comboBox_sex")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.plainTextEdit_phoneNumber = QtWidgets.QPlainTextEdit(form_register)
        self.plainTextEdit_phoneNumber.setGeometry(QtCore.QRect(180, 310, 191, 31))
        self.plainTextEdit_phoneNumber.setObjectName("plainTextEdit_phoneNumber")

        self.retranslateUi(form_register)
        QtCore.QMetaObject.connectSlotsByName(form_register)

    def retranslateUi(self, form_register):
        _translate = QtCore.QCoreApplication.translate
        form_register.setWindowTitle(_translate("form_register", "Form"))
        self.label_account.setText(_translate("form_register", "Account"))
        self.label_password_input.setText(_translate("form_register", "Input your password"))
        self.label_password_varify.setText(_translate("form_register", "Please varify your password"))
        self.label_phoneNumber.setText(_translate("form_register", "Phone Number"))
        self.label_sex.setText(_translate("form_register", "Sex"))
        self.comboBox_sex.setItemText(0, _translate("form_register", "Male"))
        self.comboBox_sex.setItemText(1, _translate("form_register", "Female"))


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
        form_register.resize(514, 564)
        self.label_account = QtWidgets.QLabel(form_register)
        self.label_account.setGeometry(QtCore.QRect(30, 20, 55, 16))
        self.label_account.setObjectName("label_account")
        self.label_password_input = QtWidgets.QLabel(form_register)
        self.label_password_input.setGeometry(QtCore.QRect(20, 110, 131, 51))
        self.label_password_input.setObjectName("label_password_input")
        self.label_password_varify = QtWidgets.QLabel(form_register)
        self.label_password_varify.setGeometry(QtCore.QRect(10, 210, 171, 21))
        self.label_password_varify.setObjectName("label_password_varify")
        self.plainTextEdit_account = QtWidgets.QPlainTextEdit(form_register)
        self.plainTextEdit_account.setGeometry(QtCore.QRect(180, 20, 161, 31))
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
        self.pushButton_register = QtWidgets.QPushButton(form_register)
        self.pushButton_register.setGeometry(QtCore.QRect(360, 510, 93, 28))
        self.pushButton_register.setObjectName("pushButton_register")
        self.label_registerAs = QtWidgets.QLabel(form_register)
        self.label_registerAs.setGeometry(QtCore.QRect(20, 450, 81, 16))
        self.label_registerAs.setObjectName("label_registerAs")
        self.comboBox_registerAs = QtWidgets.QComboBox(form_register)
        self.comboBox_registerAs.setGeometry(QtCore.QRect(200, 460, 73, 22))
        self.comboBox_registerAs.setObjectName("comboBox_registerAs")
        self.comboBox_registerAs.addItem("")
        self.comboBox_registerAs.addItem("")
        self.label_name = QtWidgets.QLabel(form_register)
        self.label_name.setGeometry(QtCore.QRect(40, 80, 55, 16))
        self.label_name.setObjectName("label_name")
        self.plainTextEdit_name = QtWidgets.QPlainTextEdit(form_register)
        self.plainTextEdit_name.setGeometry(QtCore.QRect(180, 80, 161, 31))
        self.plainTextEdit_name.setObjectName("plainTextEdit_name")

        self.retranslateUi(form_register)
        self.pushButton_register.clicked.connect(form_register.register)
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
        self.pushButton_register.setText(_translate("form_register", "Register"))
        self.label_registerAs.setText(_translate("form_register", "Register As"))
        self.comboBox_registerAs.setItemText(0, _translate("form_register", "Customer"))
        self.comboBox_registerAs.setItemText(1, _translate("form_register", "Restaurant"))
        self.label_name.setText(_translate("form_register", "Name"))


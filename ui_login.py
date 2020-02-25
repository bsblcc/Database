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
        form_login.resize(528, 418)
        form_login.setAcceptDrops(False)
        self.pushButton_regitser = QtWidgets.QPushButton(form_login)
        self.pushButton_regitser.setGeometry(QtCore.QRect(380, 20, 93, 28))
        self.pushButton_regitser.setObjectName("pushButton_regitser")
        self.plainTextEdit_account = QtWidgets.QPlainTextEdit(form_login)
        self.plainTextEdit_account.setGeometry(QtCore.QRect(150, 10, 161, 31))
        self.plainTextEdit_account.setObjectName("plainTextEdit_account")
        self.label_password = QtWidgets.QLabel(form_login)
        self.label_password.setGeometry(QtCore.QRect(40, 90, 55, 16))
        self.label_password.setObjectName("label_password")
        self.label_account = QtWidgets.QLabel(form_login)
        self.label_account.setGeometry(QtCore.QRect(40, 20, 55, 16))
        self.label_account.setObjectName("label_account")
        self.label_loginAs = QtWidgets.QLabel(form_login)
        self.label_loginAs.setGeometry(QtCore.QRect(40, 170, 55, 16))
        self.label_loginAs.setObjectName("label_loginAs")
        self.plainTextEdit_password = QtWidgets.QPlainTextEdit(form_login)
        self.plainTextEdit_password.setGeometry(QtCore.QRect(150, 80, 161, 31))
        self.plainTextEdit_password.setObjectName("plainTextEdit_password")
        self.comboBox_loginAs = QtWidgets.QComboBox(form_login)
        self.comboBox_loginAs.setGeometry(QtCore.QRect(160, 170, 73, 22))
        self.comboBox_loginAs.setObjectName("comboBox_loginAs")
        self.comboBox_loginAs.addItem("")
        self.comboBox_loginAs.addItem("")
        self.pushButton_login = QtWidgets.QPushButton(form_login)
        self.pushButton_login.setGeometry(QtCore.QRect(190, 310, 93, 28))
        self.pushButton_login.setObjectName("pushButton_login")

        self.retranslateUi(form_login)
        self.pushButton_regitser.clicked.connect(form_login.show_register)
        self.pushButton_login.clicked.connect(form_login.login)
        QtCore.QMetaObject.connectSlotsByName(form_login)

    def retranslateUi(self, form_login):
        _translate = QtCore.QCoreApplication.translate
        form_login.setWindowTitle(_translate("form_login", "Form"))
        self.pushButton_regitser.setText(_translate("form_login", "Register"))
        self.label_password.setText(_translate("form_login", "Password"))
        self.label_account.setText(_translate("form_login", "Account"))
        self.label_loginAs.setText(_translate("form_login", "Login As"))
        self.comboBox_loginAs.setItemText(0, _translate("form_login", "Customer"))
        self.comboBox_loginAs.setItemText(1, _translate("form_login", "Restaurant"))
        self.pushButton_login.setText(_translate("form_login", "Login"))


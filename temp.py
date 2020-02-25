# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_login(object):
    def setupUi(self, Dialog_login):
        Dialog_login.setObjectName("Dialog_login")
        Dialog_login.resize(482, 516)
        self.buttonBox_login = QtWidgets.QDialogButtonBox(Dialog_login)
        self.buttonBox_login.setGeometry(QtCore.QRect(-20, 330, 341, 32))
        self.buttonBox_login.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_login.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_login.setObjectName("buttonBox_login")
        self.label_loginAs = QtWidgets.QLabel(Dialog_login)
        self.label_loginAs.setGeometry(QtCore.QRect(50, 210, 55, 16))
        self.label_loginAs.setObjectName("label_loginAs")
        self.label_password = QtWidgets.QLabel(Dialog_login)
        self.label_password.setGeometry(QtCore.QRect(50, 130, 55, 16))
        self.label_password.setObjectName("label_password")
        self.plainTextEdit_account = QtWidgets.QPlainTextEdit(Dialog_login)
        self.plainTextEdit_account.setGeometry(QtCore.QRect(160, 50, 161, 31))
        self.plainTextEdit_account.setObjectName("plainTextEdit_account")
        self.label_account = QtWidgets.QLabel(Dialog_login)
        self.label_account.setGeometry(QtCore.QRect(50, 60, 55, 16))
        self.label_account.setObjectName("label_account")
        self.pushButton_register = QtWidgets.QPushButton(Dialog_login)
        self.pushButton_register.setGeometry(QtCore.QRect(0, -60, 93, 28))
        self.pushButton_register.setObjectName("pushButton_register")
        self.plainTextEdit_password = QtWidgets.QPlainTextEdit(Dialog_login)
        self.plainTextEdit_password.setGeometry(QtCore.QRect(160, 120, 161, 31))
        self.plainTextEdit_password.setObjectName("plainTextEdit_password")
        self.comboBox_loginAs = QtWidgets.QComboBox(Dialog_login)
        self.comboBox_loginAs.setGeometry(QtCore.QRect(170, 210, 73, 22))
        self.comboBox_loginAs.setObjectName("comboBox_loginAs")
        self.comboBox_loginAs.addItem("")
        self.comboBox_loginAs.addItem("")
        self.pushButton_regitser = QtWidgets.QPushButton(Dialog_login)
        self.pushButton_regitser.setGeometry(QtCore.QRect(360, 40, 93, 28))
        self.pushButton_regitser.setObjectName("pushButton_regitser")

        self.retranslateUi(Dialog_login)
        self.buttonBox_login.accepted.connect(Dialog_login.accept)
        self.buttonBox_login.rejected.connect(Dialog_login.reject)
        self.pushButton_regitser.clicked.connect(Dialog_login.showRegister)
        QtCore.QMetaObject.connectSlotsByName(Dialog_login)

    def retranslateUi(self, Dialog_login):
        _translate = QtCore.QCoreApplication.translate
        Dialog_login.setWindowTitle(_translate("Dialog_login", "Dialog"))
        self.label_loginAs.setText(_translate("Dialog_login", "Login As"))
        self.label_password.setText(_translate("Dialog_login", "Password"))
        self.label_account.setText(_translate("Dialog_login", "Account"))
        self.pushButton_register.setText(_translate("Dialog_login", "Register"))
        self.comboBox_loginAs.setItemText(0, _translate("Dialog_login", "Customer"))
        self.comboBox_loginAs.setItemText(1, _translate("Dialog_login", "Restaurant"))
        self.pushButton_regitser.setText(_translate("Dialog_login", "Register"))


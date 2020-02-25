# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_phoneNumber.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_change_phoneNumber(object):
    def setupUi(self, form_change_phoneNumber):
        form_change_phoneNumber.setObjectName("form_change_phoneNumber")
        form_change_phoneNumber.resize(400, 300)
        self.plainTextEdit_newPhoneNumber = QtWidgets.QPlainTextEdit(form_change_phoneNumber)
        self.plainTextEdit_newPhoneNumber.setGeometry(QtCore.QRect(200, 100, 161, 31))
        self.plainTextEdit_newPhoneNumber.setObjectName("plainTextEdit_newPhoneNumber")
        self.label_newPhoneNumber = QtWidgets.QLabel(form_change_phoneNumber)
        self.label_newPhoneNumber.setGeometry(QtCore.QRect(10, 110, 131, 16))
        self.label_newPhoneNumber.setScaledContents(True)
        self.label_newPhoneNumber.setWordWrap(True)
        self.label_newPhoneNumber.setObjectName("label_newPhoneNumber")
        self.pushButton_change_phoneNumber = QtWidgets.QPushButton(form_change_phoneNumber)
        self.pushButton_change_phoneNumber.setGeometry(QtCore.QRect(130, 210, 93, 28))
        self.pushButton_change_phoneNumber.setObjectName("pushButton_change_phoneNumber")

        self.retranslateUi(form_change_phoneNumber)
        self.pushButton_change_phoneNumber.clicked.connect(form_change_phoneNumber.change_phoneNumber)
        QtCore.QMetaObject.connectSlotsByName(form_change_phoneNumber)

    def retranslateUi(self, form_change_phoneNumber):
        _translate = QtCore.QCoreApplication.translate
        form_change_phoneNumber.setWindowTitle(_translate("form_change_phoneNumber", "Form"))
        self.label_newPhoneNumber.setText(_translate("form_change_phoneNumber", "New Phone Number"))
        self.pushButton_change_phoneNumber.setText(_translate("form_change_phoneNumber", "Submit"))


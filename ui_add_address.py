# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_address.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_add_address(object):
    def setupUi(self, dialog_add_address):
        dialog_add_address.setObjectName("dialog_add_address")
        dialog_add_address.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_add_address)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_newAddress = QtWidgets.QLabel(dialog_add_address)
        self.label_newAddress.setGeometry(QtCore.QRect(20, 110, 81, 21))
        self.label_newAddress.setObjectName("label_newAddress")
        self.plainTextEdit_newAddress = QtWidgets.QPlainTextEdit(dialog_add_address)
        self.plainTextEdit_newAddress.setGeometry(QtCore.QRect(120, 100, 221, 41))
        self.plainTextEdit_newAddress.setObjectName("plainTextEdit_newAddress")

        self.retranslateUi(dialog_add_address)
        self.buttonBox.accepted.connect(dialog_add_address.accept)
        self.buttonBox.rejected.connect(dialog_add_address.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_add_address)

    def retranslateUi(self, dialog_add_address):
        _translate = QtCore.QCoreApplication.translate
        dialog_add_address.setWindowTitle(_translate("dialog_add_address", "Dialog"))
        self.label_newAddress.setText(_translate("dialog_add_address", "New Addres"))


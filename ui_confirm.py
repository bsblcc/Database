# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_confirm(object):
    def setupUi(self, Dialog_confirm):
        Dialog_confirm.setObjectName("Dialog_confirm")
        Dialog_confirm.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_confirm)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog_confirm)
        self.buttonBox.accepted.connect(Dialog_confirm.accept)
        self.buttonBox.rejected.connect(Dialog_confirm.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_confirm)

    def retranslateUi(self, Dialog_confirm):
        _translate = QtCore.QCoreApplication.translate
        Dialog_confirm.setWindowTitle(_translate("Dialog_confirm", "Dialog"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_dishes.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_add_dishes(object):
    def setupUi(self, dialog_add_dishes):
        dialog_add_dishes.setObjectName("dialog_add_dishes")
        dialog_add_dishes.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_add_dishes)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_name = QtWidgets.QLabel(dialog_add_dishes)
        self.label_name.setGeometry(QtCore.QRect(20, 30, 55, 16))
        self.label_name.setObjectName("label_name")
        self.label_price = QtWidgets.QLabel(dialog_add_dishes)
        self.label_price.setGeometry(QtCore.QRect(20, 110, 55, 16))
        self.label_price.setObjectName("label_price")
        self.label_kind = QtWidgets.QLabel(dialog_add_dishes)
        self.label_kind.setGeometry(QtCore.QRect(20, 190, 55, 16))
        self.label_kind.setObjectName("label_kind")
        self.plainTextEdit_name = QtWidgets.QPlainTextEdit(dialog_add_dishes)
        self.plainTextEdit_name.setGeometry(QtCore.QRect(120, 20, 171, 31))
        self.plainTextEdit_name.setObjectName("plainTextEdit_name")
        self.plainTextEdit_kind = QtWidgets.QPlainTextEdit(dialog_add_dishes)
        self.plainTextEdit_kind.setGeometry(QtCore.QRect(120, 190, 171, 31))
        self.plainTextEdit_kind.setObjectName("plainTextEdit_kind")
        self.spinBox_price = QtWidgets.QSpinBox(dialog_add_dishes)
        self.spinBox_price.setGeometry(QtCore.QRect(130, 110, 42, 22))
        self.spinBox_price.setMaximum(500)
        self.spinBox_price.setObjectName("spinBox_price")

        self.retranslateUi(dialog_add_dishes)
        self.buttonBox.accepted.connect(dialog_add_dishes.accept)
        self.buttonBox.rejected.connect(dialog_add_dishes.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_add_dishes)

    def retranslateUi(self, dialog_add_dishes):
        _translate = QtCore.QCoreApplication.translate
        dialog_add_dishes.setWindowTitle(_translate("dialog_add_dishes", "Dialog"))
        self.label_name.setText(_translate("dialog_add_dishes", "Name"))
        self.label_price.setText(_translate("dialog_add_dishes", "Price"))
        self.label_kind.setText(_translate("dialog_add_dishes", "Kind"))


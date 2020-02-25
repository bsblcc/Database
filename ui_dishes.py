# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dishes.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_dishes(object):
    def setupUi(self, dialog_dishes):
        dialog_dishes.setObjectName("dialog_dishes")
        dialog_dishes.resize(708, 550)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_dishes)
        self.buttonBox.setGeometry(QtCore.QRect(300, 480, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget_dishes = QtWidgets.QTableWidget(dialog_dishes)
        self.tableWidget_dishes.setGeometry(QtCore.QRect(10, 10, 671, 391))
        self.tableWidget_dishes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_dishes.setColumnCount(5)
        self.tableWidget_dishes.setObjectName("tableWidget_dishes")
        self.tableWidget_dishes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dishes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dishes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dishes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dishes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dishes.setHorizontalHeaderItem(4, item)
        self.label_cost = QtWidgets.QLabel(dialog_dishes)
        self.label_cost.setGeometry(QtCore.QRect(50, 450, 55, 16))
        self.label_cost.setObjectName("label_cost")
        self.label_show_cost = QtWidgets.QLabel(dialog_dishes)
        self.label_show_cost.setGeometry(QtCore.QRect(140, 450, 55, 16))
        self.label_show_cost.setObjectName("label_show_cost")

        self.retranslateUi(dialog_dishes)
        self.buttonBox.accepted.connect(dialog_dishes.accept)
        self.buttonBox.rejected.connect(dialog_dishes.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_dishes)

    def retranslateUi(self, dialog_dishes):
        _translate = QtCore.QCoreApplication.translate
        dialog_dishes.setWindowTitle(_translate("dialog_dishes", "Dialog"))
        item = self.tableWidget_dishes.horizontalHeaderItem(0)
        item.setText(_translate("dialog_dishes", "Name"))
        item = self.tableWidget_dishes.horizontalHeaderItem(1)
        item.setText(_translate("dialog_dishes", "Kind"))
        item = self.tableWidget_dishes.horizontalHeaderItem(2)
        item.setText(_translate("dialog_dishes", "Price"))
        item = self.tableWidget_dishes.horizontalHeaderItem(3)
        item.setText(_translate("dialog_dishes", "Sales"))
        item = self.tableWidget_dishes.horizontalHeaderItem(4)
        item.setText(_translate("dialog_dishes", "Count"))
        self.label_cost.setText(_translate("dialog_dishes", "Cost"))
        self.label_show_cost.setText(_translate("dialog_dishes", "0"))


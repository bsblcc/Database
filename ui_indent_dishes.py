# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'indent_dishes.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_indent_dishes(object):
    def setupUi(self, form_indent_dishes):
        form_indent_dishes.setObjectName("form_indent_dishes")
        form_indent_dishes.resize(295, 506)
        self.tableWidget_dishes = QtWidgets.QTableWidget(form_indent_dishes)
        self.tableWidget_dishes.setGeometry(QtCore.QRect(20, 30, 261, 411))
        self.tableWidget_dishes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_dishes.setObjectName("tableWidget_dishes")
        self.tableWidget_dishes.setColumnCount(2)
        self.tableWidget_dishes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dishes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dishes.setHorizontalHeaderItem(1, item)

        self.retranslateUi(form_indent_dishes)
        QtCore.QMetaObject.connectSlotsByName(form_indent_dishes)

    def retranslateUi(self, form_indent_dishes):
        _translate = QtCore.QCoreApplication.translate
        form_indent_dishes.setWindowTitle(_translate("form_indent_dishes", "Form"))
        item = self.tableWidget_dishes.horizontalHeaderItem(0)
        item.setText(_translate("form_indent_dishes", "Name"))
        item = self.tableWidget_dishes.horizontalHeaderItem(1)
        item.setText(_translate("form_indent_dishes", "Count"))


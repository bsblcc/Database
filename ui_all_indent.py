# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Allindent.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_all_indent(object):
    def setupUi(self, form_all_indent):
        form_all_indent.setObjectName("form_all_indent")
        form_all_indent.resize(642, 786)
        self.tableWidget_currentIndent = QtWidgets.QTableWidget(form_all_indent)
        self.tableWidget_currentIndent.setGeometry(QtCore.QRect(30, 10, 601, 301))
        self.tableWidget_currentIndent.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_currentIndent.setObjectName("tableWidget_currentIndent")
        self.tableWidget_currentIndent.setColumnCount(5)
        self.tableWidget_currentIndent.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_currentIndent.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_currentIndent.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_currentIndent.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_currentIndent.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_currentIndent.setHorizontalHeaderItem(4, item)
        self.tableWidget_pastIndent = QtWidgets.QTableWidget(form_all_indent)
        self.tableWidget_pastIndent.setGeometry(QtCore.QRect(30, 390, 601, 301))
        self.tableWidget_pastIndent.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_pastIndent.setObjectName("tableWidget_pastIndent")
        self.tableWidget_pastIndent.setColumnCount(5)
        self.tableWidget_pastIndent.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pastIndent.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pastIndent.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pastIndent.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pastIndent.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pastIndent.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(form_all_indent)
        self.label.setGeometry(QtCore.QRect(200, 320, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(form_all_indent)
        self.label_2.setGeometry(QtCore.QRect(340, 710, 55, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(form_all_indent)
        self.tableWidget_currentIndent.cellDoubleClicked['int','int'].connect(form_all_indent.showCurrentIndent)
        self.tableWidget_pastIndent.cellDoubleClicked['int','int'].connect(form_all_indent.showPastIndent)
        QtCore.QMetaObject.connectSlotsByName(form_all_indent)

    def retranslateUi(self, form_all_indent):
        _translate = QtCore.QCoreApplication.translate
        form_all_indent.setWindowTitle(_translate("form_all_indent", "Form"))
        self.tableWidget_currentIndent.setSortingEnabled(True)
        item = self.tableWidget_currentIndent.horizontalHeaderItem(0)
        item.setText(_translate("form_all_indent", "Restaurant"))
        item = self.tableWidget_currentIndent.horizontalHeaderItem(1)
        item.setText(_translate("form_all_indent", "Account"))
        item = self.tableWidget_currentIndent.horizontalHeaderItem(2)
        item.setText(_translate("form_all_indent", "Address"))
        item = self.tableWidget_currentIndent.horizontalHeaderItem(3)
        item.setText(_translate("form_all_indent", "Time"))
        item = self.tableWidget_currentIndent.horizontalHeaderItem(4)
        item.setText(_translate("form_all_indent", "IID"))
        self.tableWidget_pastIndent.setSortingEnabled(True)
        item = self.tableWidget_pastIndent.horizontalHeaderItem(0)
        item.setText(_translate("form_all_indent", "Restaurant"))
        item = self.tableWidget_pastIndent.horizontalHeaderItem(1)
        item.setText(_translate("form_all_indent", "Account"))
        item = self.tableWidget_pastIndent.horizontalHeaderItem(2)
        item.setText(_translate("form_all_indent", "Address"))
        item = self.tableWidget_pastIndent.horizontalHeaderItem(3)
        item.setText(_translate("form_all_indent", "Time"))
        item = self.tableWidget_pastIndent.horizontalHeaderItem(4)
        item.setText(_translate("form_all_indent", "IID"))
        self.label.setText(_translate("form_all_indent", "Current"))
        self.label_2.setText(_translate("form_all_indent", "Past"))


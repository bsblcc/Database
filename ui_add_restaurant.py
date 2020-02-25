# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_restaurant.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_add_restaurant(object):
    def setupUi(self, form_add_restaurant):
        form_add_restaurant.setObjectName("form_add_restaurant")
        form_add_restaurant.resize(690, 574)
        self.label_name = QtWidgets.QLabel(form_add_restaurant)
        self.label_name.setGeometry(QtCore.QRect(80, 60, 55, 16))
        self.label_name.setObjectName("label_name")
        self.label_address = QtWidgets.QLabel(form_add_restaurant)
        self.label_address.setGeometry(QtCore.QRect(80, 120, 55, 16))
        self.label_address.setObjectName("label_address")
        self.label_cuisines = QtWidgets.QLabel(form_add_restaurant)
        self.label_cuisines.setGeometry(QtCore.QRect(70, 250, 55, 16))
        self.label_cuisines.setObjectName("label_cuisines")
        self.label_startTime = QtWidgets.QLabel(form_add_restaurant)
        self.label_startTime.setGeometry(QtCore.QRect(70, 350, 71, 16))
        self.label_startTime.setObjectName("label_startTime")
        self.label_endTime = QtWidgets.QLabel(form_add_restaurant)
        self.label_endTime.setGeometry(QtCore.QRect(80, 450, 71, 16))
        self.label_endTime.setObjectName("label_endTime")
        self.plainTextEdit_name = QtWidgets.QPlainTextEdit(form_add_restaurant)
        self.plainTextEdit_name.setGeometry(QtCore.QRect(230, 50, 181, 31))
        self.plainTextEdit_name.setObjectName("plainTextEdit_name")
        self.plainTextEdit_address = QtWidgets.QPlainTextEdit(form_add_restaurant)
        self.plainTextEdit_address.setGeometry(QtCore.QRect(230, 120, 181, 31))
        self.plainTextEdit_address.setObjectName("plainTextEdit_address")
        self.timeEdit_startTime = QtWidgets.QTimeEdit(form_add_restaurant)
        self.timeEdit_startTime.setGeometry(QtCore.QRect(230, 340, 118, 22))
        self.timeEdit_startTime.setObjectName("timeEdit_startTime")
        self.timeEdit_endTime = QtWidgets.QTimeEdit(form_add_restaurant)
        self.timeEdit_endTime.setGeometry(QtCore.QRect(220, 450, 118, 22))
        self.timeEdit_endTime.setObjectName("timeEdit_endTime")
        self.pushButton_submit = QtWidgets.QPushButton(form_add_restaurant)
        self.pushButton_submit.setGeometry(QtCore.QRect(490, 520, 93, 28))
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.comboBox_cuisines = QtWidgets.QComboBox(form_add_restaurant)
        self.comboBox_cuisines.setGeometry(QtCore.QRect(240, 240, 73, 22))
        self.comboBox_cuisines.setObjectName("comboBox_cuisines")
        self.comboBox_cuisines.addItem("")
        self.comboBox_cuisines.addItem("")
        self.comboBox_cuisines.addItem("")
        self.comboBox_cuisines.addItem("")
        self.comboBox_cuisines.addItem("")
        self.comboBox_cuisines.addItem("")

        self.retranslateUi(form_add_restaurant)
        self.pushButton_submit.clicked.connect(form_add_restaurant.add_restaurant)
        QtCore.QMetaObject.connectSlotsByName(form_add_restaurant)

    def retranslateUi(self, form_add_restaurant):
        _translate = QtCore.QCoreApplication.translate
        form_add_restaurant.setWindowTitle(_translate("form_add_restaurant", "Form"))
        self.label_name.setText(_translate("form_add_restaurant", "Name"))
        self.label_address.setText(_translate("form_add_restaurant", "Address"))
        self.label_cuisines.setText(_translate("form_add_restaurant", "Cuisines"))
        self.label_startTime.setText(_translate("form_add_restaurant", "Start time"))
        self.label_endTime.setText(_translate("form_add_restaurant", "End time"))
        self.pushButton_submit.setText(_translate("form_add_restaurant", "Submit"))
        self.comboBox_cuisines.setItemText(0, _translate("form_add_restaurant", "Fast Food"))
        self.comboBox_cuisines.setItemText(1, _translate("form_add_restaurant", "Chinese"))
        self.comboBox_cuisines.setItemText(2, _translate("form_add_restaurant", "French"))
        self.comboBox_cuisines.setItemText(3, _translate("form_add_restaurant", "Mexico"))
        self.comboBox_cuisines.setItemText(4, _translate("form_add_restaurant", "Italian"))
        self.comboBox_cuisines.setItemText(5, _translate("form_add_restaurant", "Japanese"))


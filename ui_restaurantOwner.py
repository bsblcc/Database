# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restaurantOwner.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_restaurantOwner(object):
    def setupUi(self, form_restaurantOwner):
        form_restaurantOwner.setObjectName("form_restaurantOwner")
        form_restaurantOwner.resize(1080, 425)
        self.label_restaurant = QtWidgets.QLabel(form_restaurantOwner)
        self.label_restaurant.setGeometry(QtCore.QRect(20, 120, 111, 41))
        self.label_restaurant.setObjectName("label_restaurant")
        self.tableWidget_restaurant = QtWidgets.QTableWidget(form_restaurantOwner)
        self.tableWidget_restaurant.setGeometry(QtCore.QRect(120, 50, 751, 311))
        self.tableWidget_restaurant.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_restaurant.setRowCount(0)
        self.tableWidget_restaurant.setColumnCount(6)
        self.tableWidget_restaurant.setObjectName("tableWidget_restaurant")
        self.pushButton_enterRestaurant = QtWidgets.QPushButton(form_restaurantOwner)
        self.pushButton_enterRestaurant.setGeometry(QtCore.QRect(920, 140, 93, 28))
        self.pushButton_enterRestaurant.setObjectName("pushButton_enterRestaurant")
        self.pushButton_add_restaurant = QtWidgets.QPushButton(form_restaurantOwner)
        self.pushButton_add_restaurant.setGeometry(QtCore.QRect(380, 370, 101, 28))
        self.pushButton_add_restaurant.setObjectName("pushButton_add_restaurant")
        self.pushButton_indents = QtWidgets.QPushButton(form_restaurantOwner)
        self.pushButton_indents.setGeometry(QtCore.QRect(630, 370, 93, 28))
        self.pushButton_indents.setObjectName("pushButton_indents")
        self.pushButton_delete_restaurant = QtWidgets.QPushButton(form_restaurantOwner)
        self.pushButton_delete_restaurant.setGeometry(QtCore.QRect(920, 230, 93, 28))
        self.pushButton_delete_restaurant.setObjectName("pushButton_delete_restaurant")

        self.retranslateUi(form_restaurantOwner)
        self.pushButton_enterRestaurant.clicked.connect(form_restaurantOwner.enter)
        self.pushButton_add_restaurant.clicked.connect(form_restaurantOwner.add_restaurant)
        self.pushButton_delete_restaurant.clicked.connect(form_restaurantOwner.delete_restaurant)
        self.pushButton_indents.clicked.connect(form_restaurantOwner.allIndents)
        QtCore.QMetaObject.connectSlotsByName(form_restaurantOwner)

    def retranslateUi(self, form_restaurantOwner):
        _translate = QtCore.QCoreApplication.translate
        form_restaurantOwner.setWindowTitle(_translate("form_restaurantOwner", "Form"))
        self.label_restaurant.setText(_translate("form_restaurantOwner", "Your restaurant"))
        self.pushButton_enterRestaurant.setText(_translate("form_restaurantOwner", "Enter"))
        self.pushButton_add_restaurant.setText(_translate("form_restaurantOwner", "Add Restaurant"))
        self.pushButton_indents.setText(_translate("form_restaurantOwner", "All Indents"))
        self.pushButton_delete_restaurant.setText(_translate("form_restaurantOwner", "Delete"))


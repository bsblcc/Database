# HOMEWORK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# TIME IS ON MY SIDE, YES IT IS
from socket import *
from myProtocol import *
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_login import Ui_form_login

from ui_register import Ui_form_register

from ui_add_restaurant import Ui_form_add_restaurant

from ui_customer import Ui_form_customer

from ui_change_phoneNumber import  Ui_form_change_phoneNumber

from ui_change_password import Ui_form_change_password

from ui_restaurantOwner import Ui_form_restaurantOwner

from ui_confirm import Ui_Dialog_confirm

from ui_add_address import Ui_dialog_add_address

from ui_restaurant import Ui_form_restaurant

from ui_add_dishes import Ui_dialog_add_dishes

from ui_order import  Ui_form_order

from ui_dishes import Ui_dialog_dishes
from ui_indent_dishes import Ui_form_indent_dishes
from ui_all_indent import Ui_form_all_indent

import struct
import simplejson
# coding=utf-8

global tcpCliSock
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)


class window_register(QtWidgets.QDialog, Ui_form_register):
    def __init__(self):
        super(window_register, self).__init__()

        self.setupUi(self)
    def register(self):

        pswi = self.plainTextEdit_password_input.toPlainText()
        pswv = self.plainTextEdit_password_varify.toPlainText()
        if pswi != pswv:
            QtWidgets.QMessageBox.information(self, "Sorry", 'passwords arent the same!')
            return

        index = self.comboBox_registerAs.currentIndex()

        #tcpCliSock = socket(AF_INET, SOCK_STREAM)
        #tcpCliSock.connect(ADDR)
        global tcpCliSock

        id = ID_REGISTER
        #data = bytes(json.dumps({'id' : 1}) + '\n', 'utf-8')
        #tcpCliSock.sendall(data)
        account = self.plainTextEdit_account.toPlainText()
        phn = self.plainTextEdit_phoneNumber.toPlainText()
        sex = self.comboBox_sex.currentText()
        name = self.plainTextEdit_name.toPlainText()

        if index == 0:



                data = {'id':id, 'type': 'customer','account' : account, 'phn' : phn, 'sex' : sex, 'psw' : pswi, 'name' : name}
                data = simplejson.dumps(data)
                data = bytes(data + '\n', 'utf-8')

                tcpCliSock.sendall(data)

                result = tcpCliSock.recv(BUFSIZ).strip()

                result = str(result, 'utf-8')

                QtWidgets.QMessageBox.information(self, "Result", result)

        else:
            #goto restaurant

            wd_add_restaurant = window_add_restaurant()
            wd_add_restaurant.exec()
            if wd_add_restaurant.success == True:
                try:
                    restName = wd_add_restaurant.plainTextEdit_name.toPlainText()
                    restAddress = wd_add_restaurant.plainTextEdit_address.toPlainText()
                    st = wd_add_restaurant.timeEdit_startTime.time().toString()
                    et = wd_add_restaurant.timeEdit_endTime.time().toString()
                    cuisines = wd_add_restaurant.comboBox_cuisines.currentText()
                    data = {'id':id,'type':'restaurant','account': account, 'phn': phn, 'sex': sex, 'psw': pswi, 'name': name, 'restName' : restName, 'restAddress':restAddress, 'st':st, 'et':et, 'cuisines':cuisines}
                    data = simplejson.dumps(data)
                    data = bytes(data + '\n', 'utf-8')
                    tcpCliSock.sendall(data)
                    result = tcpCliSock.recv(BUFSIZ).strip()
                    result = str(result, 'utf-8')
                    QtWidgets.QMessageBox.information(self, "Result", result)
                except:
                    nothing = 1


            else:
                #print ('no')
                nothing = 1
class window_all_indent(QtWidgets.QDialog, Ui_form_all_indent):
    def __init__(self):
        super(window_all_indent, self).__init__()
        self.setupUi(self)

    def showCurrentIndent(self, x, y):
        #this3
        wd_dishes = window_indent_dishes()
        iid = self.tableWidget_currentIndent.item(x, 4).text()
        id = ID_GETINDENTDISHES
        data = {'id': id, 'iid': iid}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')

        try:

            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')

            result = result.splitlines(False)
            rowCount = int(result[0])
            if rowCount == -1:
                return
            wd_dishes.tableWidget_dishes.setRowCount(rowCount)
            fieldList = ['name', 'count']

            i = 0
            for line in result[1:]:
                dic = simplejson.loads(line)
                for j in range(0, 2):
                    wd_dishes.tableWidget_dishes.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))
                i += 1

        except KeyError:

            print('keyerror')
            QtWidgets.QMessageBox.information(self, "Result", 'transformation error')
        except:
            print('error anyway')
            QtWidgets.QMessageBox.information(self, "Result", 'unknown error')
        else:
            wd_dishes.exec()

    def showPastIndent(self,x ,y ):
        wd_dishes = window_indent_dishes()
        iid = self.tableWidget_pastIndent.item(x, 4).text()
        id = ID_GETINDENTDISHES
        data = {'id': id, 'iid': iid}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')

        try:

            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')

            result = result.splitlines(False)
            rowCount = int(result[0])
            if rowCount == -1:
                return
            wd_dishes.tableWidget_dishes.setRowCount(rowCount)
            fieldList = ['name', 'count']

            i = 0
            for line in result[1:]:
                dic = simplejson.loads(line)
                for j in range(0, 2):
                    wd_dishes.tableWidget_dishes.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))
                i += 1

        except KeyError:

            print('keyerror')
            QtWidgets.QMessageBox.information(self, "Result", 'transformation error')
        except:
            print('error anyway')
            QtWidgets.QMessageBox.information(self, "Result", 'unknown error')
        else:
            wd_dishes.exec()


class window_login(QtWidgets.QDialog, Ui_form_login):
    def __init__(self):
        super(window_login, self).__init__()
        self.setupUi(self)
        self.wd_customer = 0
        self.wd_restaurantOwner = 0
    def show_register(self):
        wd_register = window_register()
        wd_register.exec()

    def login(self):
        try:
            index = self.comboBox_loginAs.currentIndex()
            #tcpCliSock = socket(AF_INET, SOCK_STREAM)
            #tcpCliSock.connect(ADDR)
            global tcpCliSock
            account =  self.plainTextEdit_account.toPlainText()
            psw = self.plainTextEdit_password.toPlainText()
            id = ID_LOGIN
        except:
            QtWidgets.QMessageBox.information(self, "Sorry", 'Login Error')
            return

        if index == 0:


            type = 'customer'
            data = {'id':id, 'type':type, 'account':account, 'password':psw}

            data = simplejson.dumps(data)
            data = bytes(data + '\n', 'utf-8')
            try:
                tcpCliSock.sendall(data)
                result = tcpCliSock.recv(BUFSIZ).strip()
                result = str(result, 'utf-8')
                if result == 'ok':
                    self.wd_customer = window_customer()
                    self.wd_customer.show()
                    self.close()


            except:
                result = 'error'

            QtWidgets.QMessageBox.information(self, "Result", result)


            #if customer

        else:
            #if restaurant
            type = 'restaurant'
            data = {'id':id, 'type':type, 'account':account, 'password':psw}
            data = simplejson.dumps(data)
            data = bytes(data + '\n', 'utf-8')
            try:
                tcpCliSock.sendall(data)
                result = tcpCliSock.recv(BUFSIZ).strip()
                result = str(result, 'utf-8')
                if result == 'ok':
                    self.wd_restaurantOwner = window_restaurantOwner()
                    self.wd_restaurantOwner.show()
                    self.close()
                    #self.wd_restaurantOwner.exec()
            except:
                result = 'error'

            QtWidgets.QMessageBox.information(self, "Result", result)

class window_add_restaurant(QtWidgets.QDialog, Ui_form_add_restaurant):
    def __init__(self):
        super(window_add_restaurant, self).__init__()
        self.setupUi(self)
        self.success = False

    def add_restaurant(self):

        #if success

        self.success = True
        self.close()
        #QtWidgets.QMessageBox.information(self, "Congrat", 'success')

class window_indent_dishes(QtWidgets.QDialog, Ui_form_indent_dishes):
    def __init__(self):
        super(window_indent_dishes, self).__init__()
        self.setupUi(self)


class window_customer(QtWidgets.QDialog, Ui_form_customer):
    def __init__(self):
        super(window_customer, self).__init__()
        self.setupUi(self)
        self.getAddress()
        self.getAllIndent()
        self.wd_order = 0
        self.tableWidget_currentIndent.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_pastIndent.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_currentIndent.setColumnHidden(3, True)
        self.tableWidget_pastIndent.setColumnHidden(3, True)

    def cancel_indent(self):
        #this3
        index = self.tableWidget_currentIndent.currentRow()
        if index < 0:
            return
        wd_confirm = window_confirm()
        result = wd_confirm.exec()
        if result != QtWidgets.QDialog.Accepted:
            return
        iid = self.tableWidget_currentIndent.item(index, 3).text()
        id = ID_CANCELINDENT



        data = {'id': id, 'iid': iid}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:

            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)

            result = str(result, 'utf-8')
        except:
            result = 'error'
        finally:
            QtWidgets.QMessageBox.information(self, "Result", result)
            self.getAllIndent()



    def getAllIndent(self):

        id = ID_GETINDENT_CUSTOMER
        data = {'id': id, 'type':'current'}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:
            print (data)
            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)

            result = str(result, 'utf-8')

            result = result.splitlines(False)
            print (result)
            rowCount = int(result[0])
            if rowCount == -1:
                return
            self.tableWidget_currentIndent.setRowCount(rowCount)
            fieldList = ['restaurant_name', 'time', 'address', 'iid']

            i = 0
            for line in result[1:]:
                dic = simplejson.loads(line)
                for j in range(0, 4):
                    self.tableWidget_currentIndent.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))
                i += 1

        except keyError:
            QtWidgets.QMessageBox.information(self, "Result", 'transformation error')
        except:
            QtWidgets.QMessageBox.information(self, "Result", 'unknown error')

        data = {'id': id, 'type': 'past'}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:

            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)

            result = str(result, 'utf-8')

            result = result.splitlines(False)
            rowCount = int(result[0])
            if rowCount == -1:
                return
            self.tableWidget_pastIndent.setRowCount(rowCount)
            fieldList = ['restaurant_name', 'time', 'address', 'iid']

            i = 0
            for line in result[1:]:
                dic = simplejson.loads(line)
                for j in range(0, 4):
                    self.tableWidget_pastIndent.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))
                i += 1

        except keyError:
            QtWidgets.QMessageBox.information(self, "Result", 'transformation error')
        except:
            QtWidgets.QMessageBox.information(self, "Result", 'unknown error')
    def show_currentIndent(self, x, y):
        #todod
        wd_dishes = window_indent_dishes()
        iid = self.tableWidget_currentIndent.item(x, 3).text()
        id = ID_GETINDENTDISHES
        data = {'id': id, 'iid': iid}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')

        try:

            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')

            result = result.splitlines(False)
            rowCount = int(result[0])
            if rowCount == -1:
                return
            wd_dishes.tableWidget_dishes.setRowCount(rowCount)
            fieldList = ['name', 'count']

            i = 0
            for line in result[1:]:
                dic = simplejson.loads(line)
                for j in range(0, 2):
                    wd_dishes.tableWidget_dishes.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))
                i += 1

        except KeyError:

            print ('keyerror')
            QtWidgets.QMessageBox.information(self, "Result", 'transformation error')
        except:
            print ('error anyway')
            QtWidgets.QMessageBox.information(self, "Result", 'unknown error')
        else:
            wd_dishes.exec()

    def show_pastIndent(self,x, y):
        wd_dishes = window_indent_dishes()
        iid = self.tableWidget_pastIndent.item(x, 3).text()
        id = ID_GETINDENTDISHES
        data = {'id': id, 'iid': iid}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')

        try:

            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')

            result = result.splitlines(False)
            rowCount = int(result[0])
            if rowCount == -1:
                return
            wd_dishes.tableWidget_dishes.setRowCount(rowCount)
            fieldList = ['name', 'count']

            i = 0
            for line in result[1:]:
                dic = simplejson.loads(line)
                for j in range(0, 2):
                    wd_dishes.tableWidget_dishes.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))
                i += 1

        except KeyError:

            print('keyerror')
            QtWidgets.QMessageBox.information(self, "Result", 'transformation error')
        except:
            print('error anyway')
            QtWidgets.QMessageBox.information(self, "Result", 'unknown error')
        else:
            wd_dishes.exec()

    def show_change_phoneNumber(self):
        wd_change_phoneNumber = window_change_phoneNumber()
        wd_change_phoneNumber.exec()

        # show edit ui

    def show_order(self):
        index = self.tableWidget_address.currentRow()
        if index < 0:
            QtWidgets.QMessageBox.information(self, "Sorry", 'Please choose an address')
            return
        address = self.tableWidget_address.item(index, 0).text()

        self.wd_order = window_order(address)
        self.wd_order.exec()
        self.getAllIndent()



        # show order ui
    def show_change_password(self):
        wd_change_password = window_change_password()
        wd_change_password.exec()
        nothing = 1
        # show edit password ui

    def finish_indent(self):
        index = self.tableWidget_currentIndent.currentRow()
        if index < 0:
            return

        iid = self.tableWidget_currentIndent.item(index, 3).text()
        id = ID_FINISHINDENT
        data = {'id': id, 'iid':iid}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:

            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)

            result = str(result, 'utf-8')
        except:
            result = 'error'
        finally:
            QtWidgets.QMessageBox.information(self, "Result", result)
            self.getAllIndent()
        # finish this indent

    def getAddress(self):
        id = ID_GETADDRESS
        data = {'id': id}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:
            print (data)
            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)

            result = str(result, 'utf-8')
            self.tableWidget_address.setHorizontalHeaderLabels(['address',])
            result = result.splitlines(False)
            rowCount = int(result[0])
            if rowCount == -1:
                return
            self.tableWidget_address.setRowCount(rowCount)

            i = 0
            for line in result[1:]:
                dic = simplejson.loads(line)


                self.tableWidget_address.setItem(i, 0, QtWidgets.QTableWidgetItem(dic['address']))
                i += 1

        except keyError:
            QtWidgets.QMessageBox.information(self, "Result", 'transformation error')
        except:
            QtWidgets.QMessageBox.information(self, "Result", 'unknown error')



    def add_address(self):
        wd_add_adress = window_add_address()
        result = wd_add_adress.exec()
        if result == QtWidgets.QDialog.Accepted:
            newAddress = wd_add_adress.plainTextEdit_newAddress.toPlainText()
            id = ID_ADDADDRESS
            data = {'id':id, 'newAddress': newAddress}
            data = simplejson.dumps(data)
            data = bytes(data + '\n', 'utf-8')
            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')
            self.getAddress()
            QtWidgets.QMessageBox.information(self, "Result", result)



    def delete_address(self):
        wd_confirm = window_confirm()
        result = wd_confirm.exec()
        if result != QtWidgets.QDialog.Accepted:
            return
        index = self.tableWidget_address.currentRow()
        address = self.tableWidget_address.item(index, 0).text()
        id = ID_DELETEADDRESS
        data = {'id': id, 'address': address}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:
            print (data)
            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            print (result)
            result = str(result, 'utf-8')
        except:
            result = 'error'
        QtWidgets.QMessageBox.information(self, "Result", result)
        self.getAddress()


class window_confirm(QtWidgets.QDialog, Ui_Dialog_confirm):
    def __init__(self):
        super(window_confirm, self).__init__()
        self.setupUi(self)

class window_add_address(QtWidgets.QDialog, Ui_dialog_add_address):
    def __init__(self):
        super(window_add_address, self).__init__()
        self.setupUi(self)


class window_change_phoneNumber(QtWidgets.QDialog, Ui_form_change_phoneNumber):
    def __init__(self):
        super(window_change_phoneNumber, self).__init__()
        self.setupUi(self)

    def change_phoneNumber(self):
        #change phonenumber
        nothing = 1

        global tcpCliSock
        newPhn = self.plainTextEdit_newPhoneNumber.toPlainText()
        id = ID_PERSONEDIT
        type = 'phone number'

        try:
            data = {'id':id, 'type':type, 'phone number':newPhn}
            data = simplejson.dumps(data)
            data = bytes(data + '\n', 'utf-8')

            print (data)
            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')
        except:
            result = 'error'
        QtWidgets.QMessageBox.information(self, "Result", result)
        self.close()





class window_change_password(QtWidgets.QDialog, Ui_form_change_password):
    def __init__(self):
        super(window_change_password, self).__init__()
        self.setupUi(self)



    def change_password(self):

        global tcpCliSock
        oldPsw = self.plainTextEdit_oldPassword.toPlainText()
        newPsw = self.plainTextEdit_newPassword.toPlainText()
        id = ID_PERSONEDIT
        type = 'password'

        try:
            data = {'id': id, 'type': type, 'old password': oldPsw, 'new password': newPsw}
            data = simplejson.dumps(data)
            data = bytes(data + '\n', 'utf-8')


            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')
        except:
            result = 'error'
        QtWidgets.QMessageBox.information(self, "Result", result)
        if result == 'ok':
            self.close()


class window_add_dishes(QtWidgets.QDialog, Ui_dialog_add_dishes):
    def __init__(self):
        super(window_add_dishes, self).__init__()
        self.setupUi(self)

class window_restaurant(QtWidgets.QDialog, Ui_form_restaurant):
    def __init__(self, restName):
        super(window_restaurant, self).__init__()

        self.setupUi(self)
        self.tableWidget_indent.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_dishes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.restName = restName
        self.get_dishes()

    def get_dishes(self):

        id = ID_GETDISHES_OWNER

        data = {'id': id, 'restName':self.restName}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:

            tcpCliSock.sendall(data)
            data = tcpCliSock.recv(BUFSIZ)
            data = str(data, 'utf-8')
            # print (data)
            fieldList = ['name', 'kind', 'price', 'sales']
            self.tableWidget_dishes.setHorizontalHeaderLabels(fieldList)
            data = data.splitlines(False)
            rowCount = int(data[0])
            if rowCount == -1:
                return
            self.tableWidget_dishes.setRowCount(rowCount)
            i = 0
            for line in data[1:]:
                dic = simplejson.loads(line)

                for j in range(0, 4):
                    self.tableWidget_dishes.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))
                i += 1

        except:
            print('exc')
            return

    def get_indents(self):
        nothing = 1
    def about_indent(self):
        nothing = 1
    def add_dishes(self):

        wd_add_dishes = window_add_dishes()
        result = wd_add_dishes.exec()
        if result != QtWidgets.QDialog.Accepted:
            return
        id = ID_ADDDISHES
        disName = wd_add_dishes.plainTextEdit_name.toPlainText()
        price = wd_add_dishes.spinBox_price.value()
        kind = wd_add_dishes.plainTextEdit_kind.toPlainText()
        try:
            data = {'id':id, 'restName':self.restName , 'disName':disName, 'price':price, 'kind':kind}
            data = simplejson.dumps(data)
            data = bytes(data + '\n', 'utf-8')
            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')
        except:
            result = 'error'
        finally:
            self.get_dishes()
            QtWidgets.QMessageBox.information(self, "Result", result)

    def edit_dishes(self):
        index = self.tableWidget_dishes.currentRow()
        if index < 0:
            return

        disName = self.tableWidget_dishes.item(index, 0).text()
        kind = self.tableWidget_dishes.item(index, 1).text()
        price = self.tableWidget_dishes.item(index, 2).text()
        wd_add_dishes = window_add_dishes()
        wd_add_dishes.plainTextEdit_name.setPlainText(disName)
        wd_add_dishes.plainTextEdit_kind.setPlainText(kind)
        wd_add_dishes.spinBox_price.setValue(int(price))
        result = wd_add_dishes.exec()
        if result != QtWidgets.QDialog.Accepted:
            return

        disName = wd_add_dishes.plainTextEdit_name.toPlainText()
        print(disName)
        kind = wd_add_dishes.plainTextEdit_kind.toPlainText()
        print (kind)
        price = wd_add_dishes.spinBox_price.value()
        print (price)
        id = ID_EDITDISHES
        try:
            data = {'id':id, 'restName':self.restName , 'disName':disName, 'price':price, 'kind':kind}
            data = simplejson.dumps(data)
            data = bytes(data + '\n', 'utf-8')
            print (data)
            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            print (result)
            result = str(result, 'utf-8')
        except:
            result = 'error'
        finally:
            self.get_dishes()
            QtWidgets.QMessageBox.information(self, "Result", result)

    def delete_dishes(self):
        wd_confirm = window_confirm()
        result = wd_confirm.exec()
        if result != QtWidgets.QDialog.Accepted:
            return
        index = self.tableWidget_dishes.currentRow()
        disName = self.tableWidget_dishes.item(index, 0).text()
        id = ID_DELETEDISHES
        data = {'id': id, 'disName': disName, 'restName' : self.restName}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:
            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')
        except:
            result = 'error'
        QtWidgets.QMessageBox.information(self, "Result", result)
        self.get_dishes()

    def about_dishes(self):
        nothing = 1


class window_restaurantOwner(QtWidgets.QDialog, Ui_form_restaurantOwner):
    def __init__(self):
        super(window_restaurantOwner, self).__init__()

        self.setupUi(self)
        self.tableWidget_restaurant.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.getRestaurant()
        self.wdList_restaurant = []

    def delete_restaurant(self):
        wd_confirm = window_confirm()
        result = wd_confirm.exec()
        if result != QtWidgets.QDialog.Accepted:
            return
        index = self.tableWidget_restaurant.currentRow()
        name = self.tableWidget_restaurant.item(index, 0).text()
        id = ID_DELETERESTAURANT
        data = {'id':id, 'name':name}
        data = simplejson.dumps(data)
        print (data)
        data = bytes(data + '\n', 'utf-8')
        try:
            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')
        except:
            result = 'error'
        finally:
            QtWidgets.QMessageBox.information(self, "Result", result)
            self.getRestaurant()

    def allIndents(self):
        #this2
        wd_all_indent = window_all_indent()
        wd_all_indent.tableWidget_pastIndent.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        wd_all_indent.tableWidget_currentIndent.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        wd_all_indent.tableWidget_pastIndent.setColumnHidden(4, True)
        wd_all_indent.tableWidget_currentIndent.setColumnHidden(4, True)

        id = ID_GETOWNERINDENT

        try:
            finished = 0
            data = {'id': id, 'finished': finished}
            data = simplejson.dumps(data)
            data = bytes(data + '\n', 'utf-8')
            tcpCliSock.sendall(data)
            data = tcpCliSock.recv(BUFSIZ)
            data = str(data, 'utf-8')
            # print (data)
            fieldList = ['restaurant', 'account','address', 'time','iid']
            data = data.splitlines(False)

            rowCount = int(data[0])

            if rowCount == -1:
                return

            wd_all_indent.tableWidget_currentIndent.setRowCount(rowCount)
            i = 0
            for line in data[1:]:
                dic = simplejson.loads(line)

                for j in range(0, 5):
                    wd_all_indent.tableWidget_currentIndent.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))
                i += 1

            finished = 1
            data = {'id': id, 'finished': finished}
            data = simplejson.dumps(data)
            data = bytes(data + '\n', 'utf-8')
            tcpCliSock.sendall(data)
            data = tcpCliSock.recv(BUFSIZ)

            data = str(data, 'utf-8')

            fieldList = ['restaurant', 'account', 'address', 'time', 'iid']
            data = data.splitlines(False)
            rowCount = int(data[0])

            if rowCount == -1:
                return

            wd_all_indent.tableWidget_pastIndent.setRowCount(rowCount)
            i = 0
            for line in data[1:]:
                dic = simplejson.loads(line)
                print (line)

                for j in range(0, 5):
                    wd_all_indent.tableWidget_pastIndent.setItem(i, j,
                                                                 QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))
                i += 1



        except KeyError:
            QtWidgets.QMessageBox.information(self, "Result", 'something wrong...')
        finally:
            wd_all_indent.exec()



    def enter(self):
        index = self.tableWidget_restaurant.currentRow()
        restName = self.tableWidget_restaurant.item(index, 0).text()

        self.wdList_restaurant.append(window_restaurant(restName))

        wd_restaurant = self.wdList_restaurant[len(self.wdList_restaurant) - 1]
        wd_restaurant.show()




    def add_restaurant(self):
        id = ID_ADDRESTAURANT
        wd_add_restaurant = window_add_restaurant()
        wd_add_restaurant.exec()
        if wd_add_restaurant.success == True:
            try:
                name = wd_add_restaurant.plainTextEdit_name.toPlainText()
                address = wd_add_restaurant.plainTextEdit_address.toPlainText()
                st = wd_add_restaurant.timeEdit_startTime.time().toString()
                et = wd_add_restaurant.timeEdit_endTime.time().toString()
                cuisines = wd_add_restaurant.comboBox_cuisines.currentText()

                data = {'id':id, 'name':name, 'address':address, 'start_time': st, 'end_time':et, 'cuisines':cuisines}

                data = simplejson.dumps(data)
                data = bytes(data + '\n', 'utf-8')
                tcpCliSock.sendall(data)
                result = tcpCliSock.recv(BUFSIZ).strip()
                result = str(result, 'utf-8')
                QtWidgets.QMessageBox.information(self, "Result", result)
                self.getRestaurant()
            except:
                nothing = 1




    def getRestaurant(self):
        id = ID_GETRESTAURANT
        data = {'id': id}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:

            tcpCliSock.sendall(data)
            data = tcpCliSock.recv(BUFSIZ)

            data = str(data, 'utf-8')
            #print (data)
            fieldList = ['name', 'address', 'cuisines', 'start_time', 'end_time', 'sales']
            self.tableWidget_restaurant.setHorizontalHeaderLabels(fieldList)
            data = data.splitlines(False)
            rowCount = int(data[0])

            if rowCount == -1:
                return

            self.tableWidget_restaurant.setRowCount(rowCount)
            i = 0
            for line in data[1:]:
                dic = simplejson.loads(line)

                for j in range(0, 5):
                    self.tableWidget_restaurant.setItem(i , j , QtWidgets.QTableWidgetItem(dic[fieldList[j]]))
                self.tableWidget_restaurant.setItem(i, 5, QtWidgets.QTableWidgetItem(str(dic[fieldList[5]])))
                i += 1

        except:

            return




class window_order(QtWidgets.QDialog, Ui_form_order):
    def __init__(self, adr):
        super(window_order, self).__init__()

        self.setupUi(self)
        self.tableWidget_restaurant.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_restaurant.setColumnHidden(5, True)
        self.address = adr
        self.getRestaurant()


        adSet = set([])
        csSet = set([])
       # print (self.tableWidget_restaurant.rowCount())
        for i in range(0, self.tableWidget_restaurant.rowCount()):
            adSet.add(self.tableWidget_restaurant.item(i, 1).text())
            csSet.add(self.tableWidget_restaurant.item(i, 2).text())

        self.comboBox_address.clear()
        self.comboBox_address.addItems(list(adSet))

        self.comboBox_cuisines.clear()
        self.comboBox_cuisines.addItems(list(csSet))
        #self.tableWidget_restaurant.horizontalHeader().sectionClicked.connect(form_indent.sortByColumn)

    def getRestaurant(self, address = "%%", cuisines = "%%", budgetMin = 0, budgetMax = 12345678):
        id = ID_SEARCHRESTAURANT

        data = {'id': id , 'address':address, 'cuisines':cuisines, 'budgetMax':budgetMax, 'budgetMin':budgetMin}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:

            tcpCliSock.sendall(data)
            data = tcpCliSock.recv(BUFSIZ)
            data = str(data, 'utf-8')
            # print (data)
            fieldList = ['name', 'address', 'cuisines', 'budget','sales', 'rid']
            data = data.splitlines(False)

            rowCount = int(data[0])
            if rowCount == -1:
                return

            self.tableWidget_restaurant.setRowCount(rowCount)
            i = 0

            for line in data[1:]:
                dic = simplejson.loads(line)

                for j in range(0, 6):

                    self.tableWidget_restaurant.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))


                i += 1



        except:

            return


    def order(self):
        index = self.tableWidget_restaurant.currentRow()
        rid = self.tableWidget_restaurant.item(index, 5).text()
        wd_dishes = window_dishes(rid)
        result = wd_dishes.exec()
        if result != QtWidgets.QDialog.Accepted:
            return
        id = ID_ADDINDENT
        dishSum = 0
        dish = ''
        for i in range(0 , wd_dishes.tableWidget_dishes.rowCount()):
            if int(wd_dishes.tableWidget_dishes.cellWidget(i, 4).value()) > 0:
                #dishSum += int(wd_dishes.tableWidget_dishes.cellWidget(i, 4).value()) * int(wd_dishes.tableWidget_dishes.item(i, 2).text())
                dishSum += 1
                name = wd_dishes.tableWidget_dishes.item(i, 0).text()
                count = wd_dishes.tableWidget_dishes.cellWidget(i, 4).value()
                dic = {'name':name, 'count':count}
                dish += simplejson.dumps(dic) + '\n'
        if dishSum == 0:
            return
        try:
            data = {'id':id,'address':self.address, 'rid':rid,'dishSum':dishSum, 'dish':dish}
            data = simplejson.dumps(data)


            data = bytes(data + '\n', 'utf-8')
            print(data)

            tcpCliSock.sendall(data)
            result = tcpCliSock.recv(BUFSIZ)
            result = str(result, 'utf-8')
        except:
            result = 'error'

        finally:
            self.filter()
            QtWidgets.QMessageBox.information(self, "Result", result)





    def filter(self):

        if self.radioButton_address.isChecked():
            address = self.comboBox_address.currentText()
        else:
            address = '%%'

        if self.radioButton_cuisines.isChecked():
            cuisines = self.comboBox_cuisines.currentText()
        else:
            cuisines = '%%'

        if self.radioButton_budget.isChecked():
            budgetMin = self.spinBox_budget_min.value()
            budgetMax = self.spinBox_budget_max.value()
        else:
            budgetMin = 0
            budgetMax = 12312312

        self.getRestaurant(address, cuisines, budgetMin, budgetMax)




class window_dishes(QtWidgets.QDialog, Ui_dialog_dishes):
    def __init__(self, rid):
        super(window_dishes, self).__init__()

        self.setupUi(self)
        self.tableWidget_dishes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.rid = rid
        self.getDishes()




    def getDishes(self):
        id = ID_GETDISHES_CUSTOMER

        data = {'id': id, 'rid': self.rid}
        data = simplejson.dumps(data)
        data = bytes(data + '\n', 'utf-8')
        try:

            tcpCliSock.sendall(data)
            data = tcpCliSock.recv(BUFSIZ)
            data = str(data, 'utf-8')
            # print (data)
            fieldList = ['name', 'kind', 'price', 'sales']
            self.tableWidget_dishes.setHorizontalHeaderLabels(fieldList)
            data = data.splitlines(False)
            rowCount = int(data[0])
            if rowCount == -1:
                return
            self.tableWidget_dishes.setRowCount(rowCount)
            i = 0
            for line in data[1:]:
                dic = simplejson.loads(line)

                for j in range(0, 4):
                    self.tableWidget_dishes.setItem(i, j, QtWidgets.QTableWidgetItem(str(dic[fieldList[j]])))


                newSB = QtWidgets.QSpinBox()
                newSB.setValue(0)
                newSB.valueChanged.connect(self.updateCost)
                self.tableWidget_dishes.setCellWidget(i, 4, newSB)
                i += 1

        except:
            print('exc')
            return

    def updateCost(self):
        sum = 0
        for i in range(0 , self.tableWidget_dishes.rowCount()):
            sum += int(self.tableWidget_dishes.cellWidget(i, 4).value()) * int(self.tableWidget_dishes.item(i, 2).text())
        self.label_show_cost.setText(str(sum))
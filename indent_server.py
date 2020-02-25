import socketserver
from db_peewee import *
from myProtocol import *
import simplejson as json
from time import ctime
# coding=utf-8
global ac
ac = 0

class myRH(socketserver.StreamRequestHandler):



    def onRegister(self, data):

        if not data:
            return
        try:
            type = data['type']
            account = data['account']
            phn = data['phn']
            sex = data['sex']
            psw = data['psw']
            name = data['name']

        except:
            return

        if type == 'customer':

            # print (account, name, psw, phn, sex)
            try:
                newPerson = Person.create(account=account, name=name, password=psw,
                                          phone_number=phn, sex=sex)
                result = 'ok'
            except:
                result = 'insert error'



        elif type == 'restaurant':
            try:
                restName = data['restName']
                restAddress = data['restAddress']
                st = data['st']
                et = data['et']
                cuisines = data['cuisines']
                sql = 'call insert_restaurantOwner (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\' , \'%s\', \'%s\');'\
                      % (account, name, psw, phn, sex, restName, st, et, restAddress, cuisines)
                print (sql)
                database.execute_sql(sql)
                result = 'yes'
            except:

                result = 'insert error'


        else:
            result = 'wrong info'
        print (result)
        self.wfile.write(bytes(result, 'utf-8'))


    def onLogin(self, data):
        global ac
        if not data:
            return

        try:
            type = data['type']
            account = data['account']
            psw = data['password']
        except:
            return

        if type == 'customer':
            try:
                if psw == Person.get(account = account).password:
                    result = 'ok'

                    ac = account

                else:
                    result = 'wrong password'
            except:
                result = 'no such account'
        elif type == 'restaurant':
            try:
                res = Restaurant.select().where(Restaurant.person_account == account)
                if not res:
                    print ('no such owner')
                    result = 'no such owner account'
                else:

                    if psw == Person.get(account=account).password:

                        ac = account
                        result = 'ok'
                    else:
                        result = 'wrong password'
            except:
                result = 'no such account'


        result = bytes(result, 'utf-8')
        self.wfile.write(result)

    def onPersonEdit(self, data):
        global ac
        if not data:
            return

        try:
            type = data['type']

            if type == 'phone number':
                newPhn = data['phone number']
                Person.update(phone_number = newPhn).where(Person.account == ac).execute()
                result = 'ok'
            elif type == 'password':
                oldPsw = data['old password']
                newPsw = data['new password']
                if Person.get(account = ac).password == oldPsw:
                    Person.update(password = newPsw).where(Person.account == ac).execute()
                    result = 'ok'
                else:
                    result = 'wrong password'
            else:
                result = 'trans error'

        except:
            result = 'error'

        result = bytes(result, 'utf-8')
        self.wfile.write(result)

    def onGetRestaurant(self):
        global ac
        try:


            sql = "select * from restaurant_run where person_account = %s"
            result = database.execute_sql(sql, (ac,))
            fieldList = ['name', 'address', 'cuisines', 'start_time', 'end_time', 'sales']
            rowCount = result.rowcount
            data = str(rowCount) + '\n'
            for tuple in result:
                dic = {}
                for i in [0,1,2,4,5]:
                    dic[fieldList[i]] = tuple[i]
                dic[fieldList[3]] = str(tuple[3])
                dic[fieldList[4]] = str(tuple[4])
                data = data + json.dumps(dic) + '\n'
            data = bytes(data, 'utf-8')



        except:
            data = '-1\n'
        #result = "".join(result)
        #print (result)
        self.wfile.write(data)

    def onAddRestaurant(self, data):
        global  ac
        try:
            name = data['name']
            address = data['address']
            st = data['start_time']
            et = data['end_time']
            cuisines = data['cuisines']
            #print (data)
            sql = "insert into restaurant (name, address, cuisines, person_account, start_time, end_time) values ('%s', '%s', '%s', '%s', '%s', '%s');" \
                  % (name, address, cuisines, ac, st,et)
            print (sql)
            database.execute_sql(sql)
            result = 'ok'
        except:
            result = 'error'

        result = bytes(result, 'utf-8')
        self.wfile.write(result)

    def onDeleteRestaurant(self, data):
        global ac

        try:
            name = data['name']
            sql = "call delete_restaurant('%s', '%s');" % (ac, name)
            #database.execute_sql(sql, (ac, name,))
            #print (sql)
            res = database.execute_sql(sql)
            print (res.rowcount)
        except KeyError:
            result = 'transformation error'

        else:
            result = 'ok' if res.rowcount != 0 else 'error\nMay have unfinished indent?'

        finally:
            result = bytes(result, 'utf-8')
            self.wfile.write(result)
    def onAddAddress(self, data):
        global ac
        result = 'insert error'
        try:
            newAddress = data['newAddress']
            Address.insert(address = newAddress, person_account = ac).execute()
        except KeyError:
            result = 'transformation error'
        else:
            result = 'ok'
        finally:
            result = bytes(result ,'utf-8')
            self.wfile.write(result)
    def onGetAddress(self):
        global ac

        try:
            sql = "select address from address where person_account = %s"
            result = database.execute_sql(sql, (ac,))
            rowCount = result.rowcount
            data = str(rowCount) + '\n'
            for tuple in result:
                dic = {}
                dic['address'] = tuple[0]
                data = data + json.dumps(dic) + '\n'

        except:

            data = '-1\n'

        finally:

            data = bytes(data, 'utf-8')
            self.wfile.write(data)
    def onDeleteAddress(self, data):
        global ac
        result = ''
        try:

            address = data['address']

            sql = "call delete_address('%s', '%s');" % (ac, address)
            print (sql)
            database.execute_sql(sql)
        except KeyError:
            result = 'transformation error'

        else:
            result = 'ok'

        finally:
            result = bytes(result, 'utf-8')
            self.wfile.write(result)

    def onAddDishes(self, data):
        global ac
        try:
            restName = data['restName']
            disName = data['disName']
            price = data['price']
            kind = data['kind']

            sql = "call add_dishes('%s', '%s' , '%s', %d, '%s');" % (ac, restName, disName, price, kind)
            #sql = "call add_dishes('%s', '%s' , '%s', %d, '%s')"
            database.execute_sql(sql)



        except KeyError:
            result = 'transformation error'
        except:
            result = 'insert error'
        else:
            result = 'ok'
        finally:
            result = bytes(result, 'utf-8')
            self.wfile.write(result)

    def onGetDishes_owner(self, data):
        global ac

        try:
            restName = data['restName']
            sql = "select dishes.name, dishes.kind, dishes.price, dishes.sales " \
                  "from restaurant join dishes on restaurant.rid = dishes.restaurant_rid " \
                  "where restaurant.person_account = %s and restaurant.name = %s"#% (ac, restName)

            #print (sql)

            result = database.execute_sql(sql, (ac,restName,))
            fieldList = ['name', 'kind', 'price', 'sales']
            rowCount = result.rowcount
            data = str(rowCount) + '\n'

            for tuple in result:
                dic = {}
                for i in range(0, 4):
                    dic[fieldList[i]] = tuple[i]

                data = data + json.dumps(dic) + '\n'

        except:
            data = '-1\n'
        finally:
            data = bytes(data, 'utf-8')
            self.wfile.write(data)


    def onDeleteDishes(self, data):

        global ac
        result = ''
        try:

            restName = data['restName']
            disName = data['disName']

            sql = "call delete_dishes(%s, %s, %s)"

            result = database.execute_sql(sql, (ac, restName, disName,))

        except KeyError:
            result = 'transformation error'

        else:
            result = 'ok'

        finally:
            result = bytes(result, 'utf-8')
            self.wfile.write(result)

    def onEditDishes(self, data):
        global ac

        try:
            restName = data['restName']
            disName = data['disName']
            price = data['price']
            kind = data['kind']

            #sql = "call add_dishes('%s', '%s' , '%s', %d, '%s');" % (ac, restName, disName, price, kind)
            sql = "call edit_dishes(%s, %s , %s, %s, %s)"
            print (ac, restName, disName, kind, price,)
            database.execute_sql(sql , (ac, restName, disName, kind, price,))



        except KeyError:
            result = 'transformation error'
        except:
            result = 'insert error'
        else:
            result = 'ok'
        finally:
            result = bytes(result, 'utf-8')
            self.wfile.write(result)

    def onSearchRestaurant(self, data):
        global ac
        try:
            address = data['address']
            cuisines = data['cuisines']
            budgetMin = data['budgetMin']
            budgetMax = data['budgetMax']

            sql = "select * " \
                  "from restaurant_open " \
                  "where address like '%s' and cuisines like '%s' and ((budget >= %s and budget <= %s) or budget is null);" \
                    %  (address, cuisines, budgetMin, budgetMax)



            result = database.execute_sql(sql)
            fieldList = ['name', 'address', 'cuisines', 'budget', 'sales', 'rid']
            rowCount = result.rowcount
            data = str(rowCount) + '\n'

            for tuple in result:

                dic = {}
                for i in range(0, 6):
                    dic[fieldList[i]] = tuple[i]

                data = data + json.dumps(dic) + '\n'

        except KeyError:
            data = '-1\n'
        finally:
            data = bytes(data, 'utf-8')
            self.wfile.write(data)

    def onGetDishes_customer(self, data):
        global ac

        try:
            rid = data['rid']
            sql = "select dishes.name, dishes.kind, dishes.price, dishes.sales " \
                  "from dishes " \
                  "where restaurant_rid = %s"  # % (ac, restName)

            # print (sql)

            result = database.execute_sql(sql, (rid,))
            fieldList = ['name', 'kind', 'price', 'sales']
            rowCount = result.rowcount
            data = str(rowCount) + '\n'

            for tuple in result:
                dic = {}
                for i in range(0, 4):
                    dic[fieldList[i]] = tuple[i]

                data = data + json.dumps(dic) + '\n'

        except:
            data = '-1\n'
        finally:
            data = bytes(data, 'utf-8')
            self.wfile.write(data)


    def onAddIndent(self, data):

        global ac
        try:
            dishSum = data['dishSum']
            if dishSum == 0:
                return
            rid = data['rid']
            dish = data['dish']
            address = data['address']
        except:

            result = 'trans error'
            return


        #database.execute_sql(sql1 , require_commit = 0)


        try:


            sql = "start transaction; "
            database.execute_sql(sql)


            sql = "insert into indent (restaurant_rid, time, address_address, address_person_account) " \
                  "values (%s, %s, '%s', '%s');   "  \
                    % (rid, 'sysdate()', address, ac)

            print (sql)
            result = database.execute_sql(sql , require_commit = 0)





            iid = result.lastrowid
            print (iid)

            dish = dish.splitlines(False)
            for line in dish:
                line = json.loads(line)
                #print (line)
                name = line['name']
                count = line['count']
                sql = "insert into indent_has_dishes (indent_iid, dishes_name , count) " \
                      "values (%s, '%s' , %s); " \
                        % (iid, name , count)
                print (sql)
                database.execute_sql(sql, require_commit = 0)



        except:
            sql = "rollback; "
            print (sql)
            database.execute_sql(sql)
            #database.rollback()
            result = "insert error \n(close while you making this order?)"
        else:
            print ('commit')
            sql = "commit; "
            database.execute_sql(sql)
            #database.commit()
            result = "ok"
        finally:



            result = bytes(result , "utf-8")
            self.wfile.write(result)


    def onGetIndent_customer(self, data):
        global ac
        try:
            type = data['type']
            if type == 'current':
                finished = 0
            elif type == 'past':
                finished = 1
            else:
                raise Exception

            sql = "select restaurant.name, indent.time, indent.address_address, indent.iid " \
                  "from indent natural join restaurant " \
                  "where indent.address_person_account = '%s' and indent.finished = %s; "\
                    % (ac, finished)

            print (sql)
            result = database.execute_sql(sql)
            fieldList = ['restaurant_name', 'time', 'address', 'iid']
            rowCount = result.rowcount

            data = str(rowCount) + '\n'

            for tuple in result:

                dic = {}
                for i in range(0, 4):
                    dic[fieldList[i]] = str(tuple[i])


                print (dic)
                data = data + json.dumps(dic) + '\n'

        except:
            data = '-1\n'
        finally:
            data = bytes(data, 'utf-8')
            self.wfile.write(data)

    def onFinishIndent(self, data):
        global ac
        try:
            iid = data['iid']

            # sql = "call add_dishes('%s', '%s' , '%s', %d, '%s');" % (ac, restName, disName, price, kind)
            sql = "call finish_indent(%s); " % (iid)


            database.execute_sql(sql)



        except KeyError:
            result = 'transformation error'
        except:
            result = 'update error'
        else:
            result = 'ok'
        finally:
            result = bytes(result, 'utf-8')
            self.wfile.write(result)
    def onGetIndentDishes(self, data):
        global  ac
        try:
            iid = data['iid']


            sql = "select dishes_name, count " \
                  "from indent_has_dishes " \
                  "where indent_iid = %s; " \
                    % (iid)

            print(sql)
            result = database.execute_sql(sql)
            fieldList = ['name', 'count']
            rowCount = result.rowcount

            data = str(rowCount) + '\n'

            for tuple in result:

                dic = {}
                for i in range(0, 2):
                    dic[fieldList[i]] = str(tuple[i])

                data = data + json.dumps(dic) + '\n'

        except:
            data = '-1\n'
        finally:
            data = bytes(data, 'utf-8')
            self.wfile.write(data)

    def onGetOwnerIndent(self, data):
        global ac
        try:
            finished = data['finished']


            sql = "select  restaurant_name, customer_account, address, time, iid " \
                  "from owner_has_indent " \
                  "where owner_account = '%s' and finished = %s; "\
                    % (ac, finished)

            print(sql)
            result = database.execute_sql(sql)
            fieldList = ['restaurant', 'account','address', 'time','iid']
            rowCount = result.rowcount

            data = str(rowCount) + '\n'

            for tuple in result:

                dic = {}
                for i in range(0, 5):
                    dic[fieldList[i]] = str(tuple[i])

                data = data + json.dumps(dic) + '\n'

        except:
            data = '-1\n'
        finally:
            data = bytes(data, 'utf-8')
            self.wfile.write(data)

    def onCancelIndent(self, data):
        #this3
        global ac
        try:
            iid = data['iid']

            # sql = "call add_dishes('%s', '%s' , '%s', %d, '%s');" % (ac, restName, disName, price, kind)
            sql = "call cancel_indent(%s); " % (iid)

            database.execute_sql(sql)



        except KeyError:
            result = 'transformation error'
        except:
            result = 'update error'
        else:
            result = 'ok'
        finally:
            result = bytes(result, 'utf-8')
            self.wfile.write(result)

    def handle(self):
        #connect = self.request

        print ('!!!!!!!!!!!!!!!!')
        global  ac
        ac = 0
        while True:


            #data = str(connect.recv(BUFSIZ), 'utf-8')
            data = self.rfile.readline().strip()

            if not data:
                continue
            data = str(data, 'utf-8')
            data = json.loads(data)
            print ('ask from %s' % ac)
            print (data)
            try:
                id = data['id']
            except:
                continue
            if isID(id):

                if id == ID_REGISTER:
                    self.onRegister(data)


                elif id == ID_LOGIN:
                    self.onLogin(data)

                elif id == ID_PERSONEDIT:
                    self.onPersonEdit(data)

                elif id == ID_GETRESTAURANT:
                    self.onGetRestaurant()

                elif id == ID_ADDRESTAURANT:
                    self.onAddRestaurant(data)

                elif id == ID_DELETERESTAURANT:
                    self.onDeleteRestaurant(data)

                elif id == ID_ADDADDRESS:
                    self.onAddAddress(data)

                elif id == ID_GETADDRESS:
                    self.onGetAddress()

                elif id == ID_DELETEADDRESS:
                    self.onDeleteAddress(data)

                elif id == ID_ADDDISHES:
                    self.onAddDishes(data)

                elif id == ID_GETDISHES_OWNER:
                    self.onGetDishes_owner(data)

                elif id == ID_DELETEDISHES:
                    self.onDeleteDishes(data)

                elif id == ID_EDITDISHES:
                    self.onEditDishes(data)

                elif id == ID_SEARCHRESTAURANT:
                    self.onSearchRestaurant(data)

                elif id == ID_GETDISHES_CUSTOMER:
                    self.onGetDishes_customer(data)

                elif id == ID_ADDINDENT:
                    self.onAddIndent(data)

                elif id == ID_GETINDENT_CUSTOMER:
                    self.onGetIndent_customer(data)

                elif id == ID_FINISHINDENT:
                    self.onFinishIndent(data)

                elif id == ID_GETINDENTDISHES:
                    self.onGetIndentDishes(data)

                elif id == ID_GETOWNERINDENT:
                    self.onGetOwnerIndent(data)

                elif id == ID_CANCELINDENT:
                    self.onCancelIndent(data)


database.connect()
tcpServ = socketserver.ThreadingTCPServer(ADDR, myRH)
tcpServ.serve_forever()


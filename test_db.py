from peewee import *
from db_peewee import *

database.connect()
try:
    newPerson = Person.create(account = 'bsblcc', name = 'nihaho', password = 'aaa', phone_number = '132323', sex = 'Male')
except:
    print ('wrong')

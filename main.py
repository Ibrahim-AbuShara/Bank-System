from accountants import Accountant
from admins import Admin
from program_user import ProgramUser
from customers import Customer
from super_customer import Super_Customer

enter = int(input('chose from 1-4 \n 1-admin \n 2-accountat \n 3-super customer \n 4-customer \n > '))
if enter == 1:
    # obj=Admin
    # obj
    # obj
    pass
elif enter == 2:
    # obj=Accountant
    # obj
    # obj
    pass
elif enter in 3:
    # obj=Super_Customer
    # obj
    # obj
    pass
if enter == 4:
    customer = Customer()
    username = input('Enter Your username')
    password = int(input('Enter Your Password'))
    customer.register(username, password, 'customer')
else:
    print(['not valid'])

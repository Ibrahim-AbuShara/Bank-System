from accountants import Accountant
from admins import Admin
from program_user import ProgramUser
from customers import Customer
from super_customer import Super_Customer

enter = int(input('chose from 1-4 \n 1-admin \n 2-accountat \n 3-super customer \n 4-customer \n > '))
# if enter == 1:
#     # obj=Admin
#     # obj
#     # obj
#     pass
# elif enter == 2:
#     # obj=Accountant
#     # obj
#     # obj
#     pass
# elif enter in 3:
#     # obj=Super_Customer
#     # obj
#     # obj
#     pass
if enter == 4:
    customer = Customer()
    username = input('Enter Your username')
    password = input('Enter Your Password')
    customer.login(username, password)
    select = int(input('choose from 1-3 \n 1-Deposit \n 2-Withdraw \n 3-Show Balance \n'))
    if select == 1:
        deposit = int(input("Write The Deposit Amount Please : "))
        customer.deposit_amount(deposit)
        customer.show_balance()
    elif select == 2:
        withdraw = int(input("Write The Withdraw Amount Please : "))
        customer.withdraw_amount(withdraw)
        customer.show_balance()
    elif select == 3:
        customer.show_balance()
else:
    print(['not valid'])

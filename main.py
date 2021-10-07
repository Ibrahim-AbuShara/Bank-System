from accountants import Accountant
from admins import Admin
from program_user import ProgramUser
from customers import Customer
from super_customer import Super_Customer
from termcolor import colored



print(colored("""\
                                 _._._                       _._._
                                _|   |_                     _|   |_
                                | ... |_._._._._._._._._._._| ... |
                                | ||| |  o  BANK System  o  | ||| |
                                |     |                     |     |
                           ())  |[-|-]| [-|-]  [-|-]  [-|-] |[-|-]|  ())
                          (())) |     |---------------------|     | (()))
                         (())())|     |                     |     |(())())
                         (()))()|[-|-]|  :::   .--.   :::   |[-|-]|(()))()
                         ()))(()|     | |~|~|  |_|_|  |~|~| |     |()))(()
                            ||  |_____|_|_|_|__|_|_|__|_|_|_|_____|  ||
                         ~ ~^^ @@@@@@@@@@@@@@/=======\@@@@@@@@@@@@@@ ^^~ ~
                             ^~^~                                ~^~^
""",'red'),'\n')
print (colored('Hello please tell us who are you:- ','green'))
enter = int(input(' 1-admin \n 2-accountat \n 3-super customer \n 4-customer \n > '))
if enter == 1:

    admin=Admin()
    username = input('Enter Your Username : ')
    password = input('Enter Your Password : ')
    admin.login(username, password)

    choice = int(input(f"hello {username} we hope you doing will \n -if you want to create a new Accountant account please press 1 \n -if you wamt you want to display all the accounts you have created pleas press 2 \n -if you want to delete any accounts please press 3 \n" ))
    if choice == 1:
        Accountantname = input('Enter Accountant Username : ')
        Accountantpass = input('Enter Accountant Password : ')
        admin.create(Accountantname, Accountantpass)

    elif choice == 2:
        admin.display()

    elif choice == 3:
        Accountantname = input('Enter Accountant Username : ')
        admin.delete(Accountantname)

    else :
        print ('Invalid Input')


#     pass
elif enter == 2:
    accountant = Accountant()
    username = input('Enter Your Username : ')
    password = input('Enter Your Password : ')
    accountant.login(username, password)

    action = int(input('what would you like to do here ?\n 1-Display\n 2- (Remove Account / Creat Account)\n'))
    if action == 1: 
        custmer_name = str(input('enter customer name to display it : '))
        accountant.desplay(custmer_name)
    elif action == 2: 
        accountant.accountAction()

elif enter == 3:

    super_Customer = Super_Customer()
    username= input('Enter Your username: ')
    password = input('Enter Your Password: ')
    super_Customer.login(username, password)
    process = int(input('choose from 1-3  \n 1-Deposit \n 2-Withdraw \n 3-Show Balance'))
    if process == 1 :
        deposit = float(input("Write The Deposit Amount Please : "))
        taxes = str(input("if agree about 29% input yes , others no  : "))
        super_Customer.deposit_amount(deposit,taxes)
        super_Customer.show_balance()

    elif process == 2 :
        withdraw = int(input("Write The Withdraw Amount Please : "))
        super_Customer.withdraw_amount(withdraw)
        super_Customer.show_balance()

    elif process == 3:
        super_Customer.show_balance()




elif enter == 4:
    customer = Customer()
    username = input('Enter Your username: ')
    password = input('Enter Your Password: ')
    customer.login(username, password)
    select = int(input('choose from 1-3 \n 1-Deposit \n 2-Withdraw \n 3-Show Balance \n'))
    if select == 1:
        deposit = float(input("Write The Deposit Amount Please : "))
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

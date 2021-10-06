from customers import  Customer


class Super_Customer(Customer):

    def __init__(self):
        super().__init__()  # inherit from Program user
        self.balance = 0  # put balance 0 on new acc
        self.AccData = []  # list to access username in the class [0] = username, [1] = password, [2] = balance
        self.logged = False


    def register(self, username, password, role):
        super().register(username, password, role)  # inherit the register func from ProgramUser
        self.AccData = [username, password, self.balance]  # put data in AccData to access it later
        with open(f"{username}.txt", "a") as f:  # append the balance variable when the user register
            f.write(f"{self.balance}\n")



    def withdraw_amount(self, amount):  # withdraw func
        if self.logged:  # user must login before access the
            self.AccData[3] = int(float(self.AccData[3]))  # AccData[2] = balance from file
            if self.AccData[3] >= (15/100)*amount + amount:
                self.AccData[3] -= (15 / 100) * amount + amount
                self.modify_line(f"{self.AccData[0]}.txt", 3, str(self.AccData[3]))  # use modify_line function
                print("\n You Withdrew:", amount)
            else:
                print("\n Your Balance Is Less Than Withdraw ")
        else:
            print("You Must Login First")


    def deposit_amount(self, amount,taxes):  # deposit func
        self.AccData[3] = int(float(self.AccData[3]))
        if self.logged:
            self.AccData[3] += amount
            self.modify_line(f"{self.AccData[0]}.txt", 3, str(self.AccData[3]))  # use modify_line function
            print("\n Amount Deposited: ", amount)
            if taxes == 'yes':
                self.AccData[3] -= (29 / 100) * amount + amount
                print("\n You Withdrew:", amount)
            else:
                self.AccData[3] -= (35 / 100) * amount + amount
                print("\n You Withdrew:", amount)
        else:
            print("You Must Login First")





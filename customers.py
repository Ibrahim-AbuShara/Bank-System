from program_user import ProgramUser


class Customer(ProgramUser):

    def __init__(self):
        super().__init__()  # inherit from Program user
        self.balance = 0  # put balance 0 on new acc
        self.AccData = []  # list to access username in the class [0] = username, [1] = password, [2] = role,
        # [3] = balance
        self.logged = False

    #  overrider Reg Method to add balance
    def register(self, username, password, role):
        super().register(username, password, role)  # inherit the register func from ProgramUser
        self.AccData = [username, password, self.balance]  # put data in AccData to access it later
        with open(f"{username}.txt", "a") as f:  # append the balance variable when the user register
            f.write(f"{self.balance}\n")

    # This func to Read The data from file and change the line you want
    @staticmethod
    def modify_line(file_open, line_tochange, new_value):
        with open(file_open, 'r') as file:
            data = file.readlines()  # read a list of lines into data
        data[line_tochange] = str(new_value) + "\n"  # line_tochange is the index num of line to change and new_value is
        # the new value to write
        with open(file_open, 'w') as file:  # open the file to write into
            file.writelines(data)  # write the new data after change in the file

    # def cash withdraw--> taxes 15%
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

    # deposit money
    def deposit_amount(self, amount):  # deposit func
        self.AccData[3] = int(float(self.AccData[3]))
        if self.logged:
            self.AccData[3] += amount
            self.modify_line(f"{self.AccData[0]}.txt", 3, str(self.AccData[3]))  # use modify_line function
            print("\n Amount Deposited: ", amount)
        else:
            print("You Must Login First")

    # def display balance
    def show_balance(self):  # function to display the balance
        if self.logged:
            print(f"Welcome {self.AccData[0]} Your Balance is : ", str(self.AccData[3]))
        else:
            print("You Must Login First")
class ProgramUser:

    def __init__(self):
        self.AccData = []          # list for passing (user_name & password) from/to  files
        self.logged = False        # login default condition

    def register(self, username, password):
        conditions = True
        # if len(str(username)) < 10:
        #     print("please enter your full name ")
        #     conditions = False
        # if len(password) < 4 or len(password) > 8:
        #     print("Enter password greater than 3 and less than 9 character")
        #     conditions = False
        if conditions:                                # user name & password are accepted
            print("Account created successfully")
            self.AccData = [username, password]       # now the list have username at loc 0 & pass at loc 1
            with open(f"{username}.txt", "w") as f:   # create new file for writing user & pass (file name = username)
                for details in self.AccData:
                    f.write(str(details) + "\n")      # passing name & pas to the new file
        else:
            print("Process Failed")                 # user name & password are not accepted


class ProgramUser:

    def __init__(self):
        self.AccData = []          # list for passing (user_name & password & role) from/to  files
        self.logged = False        # login default condition

    def register(self, username, password, role):
        conditions = True
        # if len(str(username)) < 10:
        #     print("please enter your full name ")
        #     conditions = False
        # if len(password) < 4 or len(password) > 8:
        #     print("Enter password greater than 3 and less than 9 character")
        #     conditions = False
        if conditions:                                # user name & password are accepted
            print("Account created successfully")
            self.AccData = [username, password, role]  # now the list have username at loc 0 & pass at loc 1 & role at 2
            with open(f"{username}.txt", "w") as f:    # CreateNewFileForWriting user&pass&role (file name = username)
                for details in self.AccData:
                    f.write(str(details) + "\n")       # passing name & pas & role to the new file
        else:
            print("Process Failed")                    # user name & password are not accepted

    def login(self, username, password):
        try:
            with open(f"{username}.txt", "r") as f:  # search for file with this name (exception if file doesn't exist)
                details = f.read()                   # reading name & pass & role
        except:
            print("File Doesn't Exist .. ")
            exit()
        self.AccData = details.split("\n")   # using split to get the list back
        if password == self.AccData[1]:      # remember password at loc 1
            self.logged = True               # if the password is correct then the flag now true
        if self.logged:
            print(f"{username} logged in as {self.AccData[2]}") # remember role at loc 2
        else:
            print("Wrong details")
            exit()

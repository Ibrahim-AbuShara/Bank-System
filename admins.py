from os import remove
from program_user import ProgramUser

class Admin(ProgramUser):                 #inhert from Prgram_User loin/register
  id = 1000 
  users = []
  def __init__(self):                     #ovride 'Id' in __init
    super().__init__()
    Admin.id += 1 
    Admin.users.append(self.AccData[0])


  def login (self, username, password):
      super().login(username, password)   # inherit from program_user
      if self.AccData[2]!='admin':        # check if role is admin
          exit()



  def create (self, username, password): #create new accouts for Accountats
     super().register(username, password, role= 'accountant')


  def display (self): #can acss all Accountats and desplay it
     for i in range(Admin.users):
           print(Admin.users[i] , '\n')



  def delete (self, username ): #delete new accouts for Accountats
      try:
         with open(f"{username}.txt", "r") as f:  # search for file with this name (exception if file doesn't exist)
            details = f.read()                   # reading name & pass & role
      except:
         print("USER DOESN'T EXIST")
         exit()

      self.AccData = details.split("\n")

      if self.username == self.AccData [0] and self.AccData[2]=='admin': #check if username exist and admin
            remove(f'{username}.txt')
            print('customer successfly removed!')
      else : 
         print("USER DOESN'T EXIST")


from os import remove
from re import search
from program_user import ProgramUser
from customers import Customer

class Admin(ProgramUser):                 #inhert from Prgram_User loin/register
  id = 1000 
  def __init__(self):                     #ovride 'Id' in __init
    super().__init__()
    Admin.id += 1 


  def login (self, username, password, role):
      super().login(username, password,role)   # inherit from program_user
      if self.AccData[2]!='admin':        # check if role is admin
          exit()



  def create (self, username, password): #create new accouts for Accountats
     super().register(username, password, role= 'accountant')
     with open("Accountats.txt", "a") as f:
      f.write(str(self.AccData[0]) + "\n")



  def display (self): #can acss all Accountats and desplay it
       with open("Accountats.txt", "r") as f:
          details = f.read() 
          print(details)



  def delete (self, username ): #delete new accouts for Accountats
      try:
         with open(f"{username}.txt", "r") as f:  # search for file with this name (exception if file doesn't exist)
            details = f.read()                   # reading name & pass & role
      except:
         print("USER DOESN'T EXIST")
         exit()

      self.AccData = details.split("\n")

      with open("Accountats.txt", "r") as f:
          details = f.read() 
          

      if search(username,details):
         rep = details.replace(username , "")
         with open("Accountats.txt", "w") as f:
            f.write(str(rep) + "\n")

      else : 
          print("USER DOESN'T EXIST")

      if username == self.AccData [0] and self.AccData[2]=='accountant': #check if username exist and accountant
            remove(f'{username}.txt')
            print(' Accountats removed!')
      

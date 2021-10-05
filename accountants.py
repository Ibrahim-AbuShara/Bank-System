from os import remove
from program_user import ProgramUser

class Accountant(ProgramUser):
   #inhert from Prgram_User loin/creat
   #ovride 'Id' in __init
   def __init__(self): 
      super().__init()
   
   #can acss all customers and desplay it ONLY WITH USER NAME
   def login(self, user_name):
      try:
         with open(f"{user_name}.txt", "r") as f:  # search for file with this name (exception if file doesn't exist)
            details = f.read()                   # reading name & pass & role
         
         self.AccData = details.split("\n")
         print(f"{user_name} logged in as {self.AccData[2]}") # remember role at loc 2
         print(f'customer name : {user_name}\nrole : {self.role}')
      except:
         print("USER DOESN'T EXIST")
         exit()


   #creat/dleate new accouts for customers
   # overriding register method from program_user
   def accountAction(self, username):
      choise = str(input('would you like to (remove / creat) an accountn ?'))
      
      if choise == 'creat':
         super().register(self,username,password,role)
      
      elif choise == 'remove':
         try:
            remove(f'{username}.txt')
            print('customer successfly removed!')
         except:
            print("USER DOESN'T EXIST")
            exit()
      else:
         print("wrong input please try again later ")
         
   pass


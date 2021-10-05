# ------------------------------------------------------------- BAD CODE DON't USE IT _______________________________________________________________________________#
from os import remove
from program_user import ProgramUser

class Accountant(ProgramUser):
   #inhert from Prgram_User loin/creat
   #ovride 'Id' in __init
   def __init__(self): 
      super().__init__()  # inherit from Program user
   
   #can acss all customers and desplay it ONLY WITH USER NAME
   def login(self, user_name):
      try:
         with open(f"{user_name}.txt", "r") as f:  # search for file with this name (exception if file doesn't exist)
            details = f.read()                   # reading name & pass & role
      except:
         print("USER DOESN'T EXIST")
         exit()

      self.AccData = details.split("\n")
      print(f'customer name : {user_name}\nrole : {self.AccData[2]}')


   #creat/dleate new accouts for customers
   # overriding register method from program_user
   def accountAction(self):
      choise = str(input('would you like to (remove / creat) an accountn ?\n >'))
      
      if choise == 'creat':
         acc_name = str(input('Enter Account Name : '))
         password = str(input('Enter Password : '))
         role = str(input('Enter Role : '))
         super().register(acc_name,password,role)
      
      elif choise == 'remove':
         username = str(input('enter customer name to get his ass: '))
         try:
            remove(f'{username}.txt')
            print('customer successfly removed!')
         except:
            print("USER DOESN'T EXIST")
            exit()
      else:
         print("wrong input please try again later ")
         
   pass


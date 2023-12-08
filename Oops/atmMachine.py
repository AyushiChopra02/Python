class Atm:
    # constructor mtlb agr h jb run krege vo print hoga e
 def __init__(self):
  self.pin = ""
  self.balance= 0
  self.menu()
  def menu(self):
#    triple iverted cmma for mutiple strings
   user_input =  input("""
                hello, how would you like to proceed?
                      1. enter 1 to create pin 
                      2. enter 2 to deposit
                      3. enter 3 to withdraw
                      4. enter 4 to check balance
                      5. enter 5 to exit


""")
   if user_input == "1 ":
    self.create_pin()
   elif user_input == "2":
    print("withdraw")
   elif user_input == "3":
    print("deposit")
   else:print("bye ")  
   def create_pin(self):
    self.pin = input("enter your pin")
    print("pin set scsfly  ") 

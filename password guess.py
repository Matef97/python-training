mypassword = "tefa@yahoo.com"
password = input("Enter the password ")
trial = 4

while mypassword != password and trial > 1 :
      trial-=1
      print(f"Wrong password {'last ' if trial==1 else trial} chance left" )
      password = input("Enter the password ")
else :
    if mypassword != password :
        print("Access Denied") 
    else :
      print("congraratulation your access accepted")





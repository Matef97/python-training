# Practial MemberShip Control
# List of Admins
admins =["Mostafa","Ahmed","Sayed","Taher","Mona"]
#Login step
name = input("Enter your name : ").capitalize()
# if name in admins
if name in admins :
    print(f"Hello Mr {name} \nWelcome to our application")
    option = input("Do you want to update | delete ? ").lower()
    if option == "update" :
        admins[admins.index(name)] = input("Enter your new name : ")
        print("you already update your name")
        print(admins)
    elif option == "delete" :
         admins.remove(name)
         print("you are not admin any more")
         print(admins)
    else :
        print("you entered a wrong option") 
#If name not in admins        
else :
     desire = input("Do you want to be an admin Y|N ? ").lower() 
     if desire =="y" or desire == "yes" :
        admins.append(name) 
        print(admins)
     else :
       print("the admins will be the same ") 
       print(admins)   
print("#"*80)                  

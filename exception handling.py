my_file = None
tries = 4
while tries>0 :
    try :
        print(f"you have {tries} tries left ")
        file_path = input("Enter your file path :")
        my_file =open(file_path,'r')
        print(my_file.read())
        break
    except FileNotFoundError:
        tries-=1
        print("you entered a wrong path ")
    except :
        print('found Error')  
    finally :
        if my_file is not None :
            print("the file opened")      
else :
    print("you finished all tries")

mysites =[]
maxsites = 5
while maxsites > 0 :
   website =  input("Enter your new website without https:// ").lower()  
   mysites.append(website) 
   print(mysites)
   maxsites-=1
print("your bookmark is full")
if len(mysites)>0 :
    mysites.sort() 
    index = 0
    while index < len(mysites) :
        print(mysites[index])
        index+=1
print("This is the end".center(80,'#'))        

from cgi import print_arguments


skills1 = ('html','css','javascript','c','c#')
skills2 = {"c++":"50%","python":"60%","git":"33%"}
def showSkills(name,*skillswithot,**skillwith) :
    print(f"Hello {name} \nyou have these skills :")
    print("your skills without progress are")
    for i in skillswithot :
        print( i.upper())
    print("your skills with progress are ")   
    for j,k in skillwith.items() :
        print(f"{j.upper()} => {k}")

showSkills("Tefa",*skills1,**skills2)        
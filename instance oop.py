from re import M
from abc import abstractmethod,ABCMeta


class Member() :
    non_perm_names =["animal","shit"]
    user_num = 0
    @classmethod
    def show_count(cls):
        print(f'we have {Member.user_num} users in our system')
    @staticmethod
    def say_hello() :
        print('Hello everyone')    

    def __init__(self,f_name,s_name,l_name,gender) -> None:
        self.fname =  f_name
        self.mname =  s_name
        self.lname =  l_name
        self.gender = gender
        Member.user_num += 1

    def full_name(self)  :
        if self.fname  in Member.non_perm_names :
            raise ValueError('you entered a wrong name') 
        else   : 
           return f'Your full name is {self.fname} {self.mname} {self.lname}'  
    def greet_msg(self) :
        if self.gender == "Male" :
            return f"Hello Mr {self.fname}"  
        elif self.gender == "Female" :
            return f"Hello Miss {self.fname}"
        else :
            return f"Hello  {self.fname}" 
    def get_info(self) :
        return f'{self.greet_msg()}\n{self.full_name()}' 

class SpecialMember(Member):
    def __init__(self, f_name, s_name, l_name, gender,salary) -> None:
        super().__init__(f_name, s_name, l_name, gender)  
        self.salary =salary      

class SuperMember(SpecialMember) :
    pass
m1 = SpecialMember("Mostafa",'Atef','Zayed',"Male",7000)   
m2 = Member("Mona",'Elsayed','Eldaly','Female') 
m3 = Member('Ahmed','Atef','Zayed',"hassana")
m4 = Member('shit','Atef','Zayed',"hassana")
print(m1.get_info())
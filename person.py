class Person :
    fname = '####'
    lname = '####'
    age = 0000
    gender = '!'
    def __init__(self) -> None:
        pass
    @property
    def get_name(self):
        return self.fname+' '+self.lname
    def get_info(self):
        print(f'your name is {self.get_name()} and your age is {self.age}')    
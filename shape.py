class Shape :
    def __init__(self) -> None:
        pass
        
    def read(self):
        name = input("enter the shape name : ")
        return name
    def get_area(self):
        pass
    def get_perimeter(self):
        pass
    def get_characteristics(self):
        print(f"the area of {self.read()} is {self.get_area()} cm^2 ")
        print(f"and the perimeter  is {self.get_perimeter()} cm ")


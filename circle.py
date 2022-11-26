from shape import Shape
class Circle(Shape):
    def __init__(self,r) -> None:
        super().__init__()
        self.r = r
    def read(self):
        return super().read()    
    def get_area(self):
        return 3.14*self.r*self.r
    def get_perimeter(self):
        return 2*3.14*self.r
    def get_characteristics(self):
        return super().get_characteristics()            
class Polygon:
    # private objects
    __height=None
    __width=None

    # Sets the value of private variables
    def __init__(self,height, width):
        self.__width=width
        self.__height=height
    
    # Give the access of private member of a class
    def get_height(self):
        return self.__height
    def get_width(self):
        return self.__width
    

class Rectangle(Polygon):
    def __init__(self, height, width):
        Polygon.__init__(self,height,width)
    def area(self):
        return self.get_height() * self.get_width()
    
class Triangle(Polygon):
    def __init__(self, height, width):
        Polygon.__init__(self,height,width)
    def area(self):
        return self.get_height() * self.get_width() / 2

rect=Rectangle(10,20)
print(rect.area())

tri=Triangle(15,25)
print(tri.area())


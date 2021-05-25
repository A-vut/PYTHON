class Rectangle:
    def __init__(self, height, width):
        self.__height=height
        self.__width=width
    
    def set_height(self, height):
        self.__height=height
    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width=width
    def get_width(self):
        return self.__width
    
    def get_area(self):
        return self.__height * self.__width
    
    def public_method(self,a,b):
        self.__private_value(a,b)

    def __private_value(self,a,b):
        print(self.__height, self.__width,a,b)

rect1=Rectangle(10,20)
# rect1.__height=15
print(rect1.get_area())
rect1.set_height(15)
print(rect1.get_area())

rect2=Rectangle(20,20)
# print(rect2.__height)
print(rect2.get_height())
print(rect2.get_area())

# rect2.__private_value()
rect2.public_method(5,55)




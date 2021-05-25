class Polygon:
    # private objects
    __height=None
    __width=None

    # Sets the value of private variables
    def set_values(self,height, width):
        self.__width=width
        self.__height=height
    
    # Give the access of private member of a class
    def get_height(self):
        return self.__height
    def get_width(self):
        return self.__width
    

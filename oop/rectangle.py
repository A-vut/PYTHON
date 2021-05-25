from polygon import Polygon
from shape import Shape

class Rectangle(Polygon,Shape):
    def __init__(self, height, width, color):
        self.set_values(height,width)
        self.set_color(color)
    def area(self):
        return self.get_height() * self.get_width()
    def color(self):
        return self.get_color()
   




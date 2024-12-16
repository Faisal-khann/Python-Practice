class shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

    
class Rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display_rect(self):
        print(f"Area of Rectangle = {self.area()}")
        print(f"Perimeter of Rectangle = {self.perimeter()}")

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def display_cir(self):
        print(f"Area of circle = {self.area()}")
        print(f"Perimeter of circle = {self.perimeter()}")
    
# create an object
shape1 = Rectangle(10, 5)
shape1.display_rect()

shape2 = Circle(2)
shape2.display_cir()

# for shape in shape1:
#     print(f"Area: {shape.area()}, {shape.perimeter()}")

class Shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0
    
    def display(self):
        print(f"Shape: {self.__class__.__name__}")
        print(f"Area = {self.area()}")
        print(f"Perimeter = {self.perimeter()}")
        print()

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create objects
shape1 = Rectangle(10, 5)
shape1.display()

shape2 = Circle(2)
shape2.display()

'''
1. Added a single display method in the base class (Shape) to avoid duplication and improve maintainability.
2. Used self.__class__.__name__ to dynamically retrieve the class name for display purposes.
'''

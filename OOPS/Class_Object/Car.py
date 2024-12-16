class car:
    # constructor
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

    # method 
    def display_info(self):
        return f"{self.brand} {self.name}"
    
# Create an object
car1 = car("Toyoya", "Supra")
print(car1.display_info())

car2 = car("Lambourghini", "urus")
print(car2.display_info())

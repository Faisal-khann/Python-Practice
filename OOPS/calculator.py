class Calculator:
    def __init__(self, n):
        self.n = n
    
    #function define
    def square(self):
        print(f'Square of {self.n} is {self.n*self.n}')

    def cube(self):
        print(f'Cube of {self.n} is {self.n*self.n*self.n}')
    
    def squareroot(self):
        print(f'Squareroot of {self.n} is {self.n**1/2}')

    @staticmethod
    def greet():
        print("Hello Charlie")


a = Calculator(4)
a.square() # function call
a.cube()
a.squareroot()
a.greet()

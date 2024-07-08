# Here is the introduction of basic of class and object in python
class student:

    # constructor 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Methods 
    def welcome(self):
        print("Welcome", self.name)

    # Method to find avg marks
    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        
        print("hii", self.name, "your average marks is:", sum/3)

# object
s1 = student("Tom", [91, 65, 55]) # marks store in the form of list
s1.avg_marks()
s1.welcome() # call the methods
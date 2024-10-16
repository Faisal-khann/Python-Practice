# A constructor is a special type of method (function)-
# -which is used to initialize the instance members of the class.
# In C++ or Java, the constructor has the same name as its class,
# but it treats constructor differently in Python. It is used to create an object.


# Example of constructor, class and objects in python
class Employee:
    company_Name = "Microsoft"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def getInfo(self):
        # print("ID of the Employee:%d\n Name of the Employee:%s" % (self.id, self.name))
        print(f"Id of the {self.name} is:", self.id)
        print(f"Name of the Employee is:", self.name)
        print("Working company is: ", Employee.company_Name)
        print()


# object
emp1 = Employee("John", 101)
emp1.getInfo()

emp2 = Employee("Charlie", 102)
emp2.getInfo()

emp3 = Employee("Em", 103)
emp3.getInfo()
# print("Working Company is:",Employee.company_Name)




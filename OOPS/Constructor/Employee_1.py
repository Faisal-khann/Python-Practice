''' A constructor is a special type of method (function)-
-which is used to initialize the instance members of the class.

In C++ or Java, the constructor has the same name as its class,
but it treats constructor differently in Python. It is used to create an object.
'''

class Employee:
    company_Name = "Microsoft"

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def getInfo(self):
        # print("ID of the Employee:%d\n Name of the Employee:%s" % (self.id, self.name))
        print(f"Name of the Employee is:", self.name)
        print(f"Id of the {self.name} is:", self.id)
        print(f"Salary of {self.name} is:", self.salary)
        print("Working company is: ", Employee.company_Name)
        print()

    @staticmethod
    def leaveMsg():
        print("Leave on Sunday and Monday")


# create an object
emp1 = Employee("John", 101, 40000)
emp1.getInfo()

emp2 = Employee("Charlie", 102, 55000)
emp2.getInfo()

emp3 = Employee("Em", 103, 60000)
emp3.getInfo()

Employee.leaveMsg()
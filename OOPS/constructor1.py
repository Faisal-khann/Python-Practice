class Employee:
    company = "Google"
    position = "SDE-1"

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary 


    def getInfo(self):
        print(f"Name of the Employee with Id {self.id} is:", self.name)
        print(f'Id of {self.name} is:', self.id)
        print(f'Salary of {self.name} is:', self.salary)
        print("Working Company is: ", self.company)
        print("Job profile is: ", self.position)
        print()

    @staticmethod
    def greet():
        print("Hello guys")

# print("Working Company is: ",Employee.company)
# print("Job profile is: ", Employee.position)
emp1 = Employee("Charlie", 101, 120000)
emp1.getInfo()

emp2 = Employee("John", 102, 150000)
emp2.getInfo()



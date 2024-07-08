class Employee:
    company = "Meksoft"

    # define constructor
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    # define method
    def display(self):
        print(f"ID: {self.id}, NAME: {self.name}, SALARY: {self.salary}, COMPANY: {self.company}")
        print()


if __name__ == "__main__":
        emp1 = Employee(101, "Tom", 45000)
        emp2 = Employee(102, "Roy", 50000)
        emp3 = Employee(103, "Alex", 42000)

        # Call the display method
        emp1.display()
        emp2.display()
        emp3.display()
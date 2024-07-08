class Programmer:
    company = "Microsoft"

    #constructor
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin



p = Programmer("Charlie", 125000, 846004)
print(p.name, p.salary, p.pin, p.company)

s = Programmer("Sam", 115000, 846005)
print(s.name, s.salary, s.pin, s.company)

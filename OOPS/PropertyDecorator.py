class Student:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem

    @property
    def percentage(self):
        return str((self.phy+self.math+self.chem)/3) + "%"
    
std = Student(98, 78, 96)
# print(std.percentage)
std.math = 95
print(std.percentage)
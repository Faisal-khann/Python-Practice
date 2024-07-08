# When we declare a variable inside a class, but outside the method, it is called a static or class variable.
# It can be called directly from a class but not through the instances of a class.

# static method -It can be called directly from the class by reference to a class name.
# static method is the method which is don't use the self parameter
# using the @staticmethod Decorator
class Marks:
    @staticmethod
    def Math_num(a, b):
        return a+b
    
    @staticmethod
    def Eng_num(a, b):
        return a+b
    
    @staticmethod
    def Sci_num(a, b):
        return a+b
    
#print the total marks
print("Total Marks in Math is",Marks.Math_num(88, 73))
print("Total Marks in English is",Marks.Eng_num(82, 68))
print("Total Marks in Science is",Marks.Sci_num(88, 94))

# Example 2
class Person:
    @staticmethod
    def Age():
        age = int(input("Enter the age number: "))
        if age < 18:
            print('should not eligible for vote')
        else:
            print('Eligible for vote')

Person.Age()







     

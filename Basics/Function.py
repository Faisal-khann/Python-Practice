# Function - A function is a group of statement performing a specific task.

# Function definition
def avg():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    average = (a + b + c)/3
    print(average)

# Function call
avg()

# *****Concept of Main Function*****
# Main Function is used to call the "def" function

# Q-> Perform Even Odd
number = int(input("Enter the number:"))
def findEvenOdd(number): #function with argument
    if number % 2 == 0:
        print("Number is Even")
    else:
      print("Number is odd")

if __name__ == '__main__':
    findEvenOdd(number)
    

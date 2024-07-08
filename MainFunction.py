# Main Function is used to call the "def" function

# Perform Even Odd
number = int(input("Enter the number:"))
def findEvenOdd(number):
    if number % 2 == 0:
        print("Number is Even")
    else:
      print("Number is odd")

if __name__ == '__main__':
    findEvenOdd(number)
    


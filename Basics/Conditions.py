# In python there are basically two types of condition statement 
# 1. if-else statement
# 2. elif statement

# Example 1 with f escape 
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

def greaterNum(a, b):
 if a > b: 
    print(f'{a} is greater than {b}')
 elif a == b:
    print(f'{a} is equal to {b}')
 else:
    print(f'{a} is smaller than {b}')

if __name__ == '__main__':
   greaterNum(a, b)

print(' ')

# Example 2 
age = int(input("Enter the value of age: "))

def canVote(age):
 if age > 18:
    print("He is elgibile for vote")
 elif age == 18:
   print("He is Eligible to apply voter iD")
 else:
   print("He can not eligible for vote")

if __name__ == '__main__':
  canVote(age)

print(' ')

# Example 3
age = int(input('Enter the Age: '))

def canDrive(age):
  if age >=18:
    print("yes, He is eligible for drive")
  else:
    print('No, He cannot eligible for drive')

if __name__ == '__main__':
  canDrive(age)

    

      


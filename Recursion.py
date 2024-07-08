def factorial(n):
    if n == 0 or n ==1: # factorial 0 is 1 and fact 1 is 1 
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a number"))
print(f"Factorial of {n} is: {factorial(n)} ")
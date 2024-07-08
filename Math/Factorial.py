# Find Factorial by using python function and main function
n = int(input("Enter the value of n:"))

def findFact(n):
 fact = 1
 for i in range(1, n+1):
  fact = fact*i
 print(f'Factorial of {n} is: ',fact)

if __name__ == '__main__':
  findFact(n)  


# for i in range(1, n+1):
#         fact = fact*i
# print(f'Factorial of {n} is: ', fact)
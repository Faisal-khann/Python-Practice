#check which number is prime or not
n =int(input('Enter the value of number:'))
temp = 0 # temp is used to store

for i in range(2, n): # range of i is from 2 to n-1;
    if (n % i) == 0:
        temp = temp+1

if (temp > 0):
    print(f"{n} is Not prime")

else:
    print(f"{n} is prime")
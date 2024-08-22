# perform prime number by function
num = int(input('Enter the number: '))
def findPrime(num):
    temp = 0
    for i in range(2 , num): # range of i is from 2 to num-1;
        if num % i == 0:
            temp = temp + 1

    if temp > 0 :
        print(f'{num} is not prime')
    else:
        print(f'{num} is Prime Number')

if __name__ == '__main__':
    findPrime(num)
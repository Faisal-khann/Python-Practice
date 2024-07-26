#Swap two numbers without using a third variable.
a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))

def SwapNum(a, b):
    a = a+b
    b = a-b
    a = a-b

    print("a =", a)
    print("b =", b)

if __name__ == '__main__':
    SwapNum(a, b)




# Problem 1
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# problem 2: Greet the person whose name start with s
list = ["Harry", "Soham", "Sachin", "Rahul"]

for name in list:
    if(name.startswith("S")):
        print(f"Hello {name}")

# Problem 3: Prime Number
n = int(input("Enter a number"))

for i in range(2, n):
    if(n % i)==0:
        print("Number is Not prime")
        break
    else:
        print("Number is Prime")




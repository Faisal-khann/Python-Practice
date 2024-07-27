# In python there are two type of looping statement
# 1.For loop
# 2.While loop

# Example of while loop
count = 1
while(count<=5):
    print(count)
    count +=1
    # count = count + 1

print(' ')

# Example of for loop
n = 6
for i in range(1, n):
    print(i)


# Example of List, Tuple, String, and Dictionary Iteration Using for Loops

print("List Iteration")
list = ["BMW", "Bugati", "Jaguar"]
for i in list:
	print(i)
	
print("\nTuple Iteration")
t = ("BMW", "Bugati", "Jaguar")
for i in t:
	print(i)
	
print("\nString Iteration")
s = "Charlie"
for i in s:
	print(i)
	
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("%s %d" % (i, d[i]))
	
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
	print(i),

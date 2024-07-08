# Sets are used to store multiple items in a single variable.
# Sets are written with curly brackets.
# Set items are unordered, unchangeable, and do not allow duplicate values.

myset = {"Mekkah", "Madinah", "Jordan", "Riyadh"}
# Access the set by using for loop 
print('Here is the set:')
for i in myset:
    print(i)
print(' ')
# Add item in set
myset.add("Arab")
print(myset)
print(' ')

# Join two set by union and update() method
s1 = {"a", "b", "c"}
s2 = {10, 15, 20}
s1.update(s2) # Update() method
print(s1)

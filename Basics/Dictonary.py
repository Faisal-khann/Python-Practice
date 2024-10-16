# Dictionaries are used to store data values in key:value pairs.
# A Dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Perform Multiple operation on Dictionaries
mydict = {"Brand": "Ford", "Model": "Mustang", "year": 1964}
print(mydict)
print("Length of the given Dictnory is: ", len(mydict))
print("Type of the given Dictnory is: ", type(mydict))
# Add items by using update() method
mydict.update({"Color": "Red"})
print(mydict)
# We can change the value of a specific item by referring to its key name:
# mydict["year"] = 2008 or we can use mydict.update({"year": 2008})
mydict.update({"year": 2008})
print(mydict)
print(' ')

# Iterate the Dictonaries by for loop
thisdect = {"BMW", "Lambourghini", "Ferrari", "GTR"}
for i in thisdect:
    print(i)

# unordered, unchangeable, and do not allow duplicate values

aset = {"apple", "banana", "orange"}
print(aset)

conset = set(("apple", "banana", "orange")) # constructor

# accessing

asetwithdupe = {"apple", "banana", "banana"}
print(asetwithdupe)

# adding

aset.add("cherry")
print(aset)

aset.add("apple") # a dupe value
print(aset)

# removing

aset.remove("banana")
print(aset)
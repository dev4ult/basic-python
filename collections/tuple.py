# ordered, unchangeable, and allow duplicates

atuple = ("apple", "banana", "orange")
print(atuple)

contuple = tuple(("kiwi", "melon", "mango")) # constructor
print(contuple)

# accessing

listOne = atuple[0] 
print(listOne)

listOutOfIndex = atuple[-1]
print(listOutOfIndex)

fruitlist = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("list 3 - 5 : ", fruitlist[2:5]) # sub list
print("start from 5 : ", fruitlist[4:]) # start from 5
print("end to 5 : ", fruitlist[:5]) # end to 5

# updating

atuple += contuple
print(atuple)

alist = list(atuple) # changing to a list
alist.append("orange")
thistuple = tuple(alist)
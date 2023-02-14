# ordered, changeable, and allow duplicates

alist = ["list1", "list2", "list3"]
print(alist)

conlist = list(("test", "test2")); # constructor
print(conlist)

allowdupelist = ["test1", "test2", "test2"];
print(allowdupelist)

listlen = len(alist); # length of list
print(listlen)

# accessing

listOne = alist[0] 
print(listOne)

listOutOfIndex = alist[-1]
print(listOutOfIndex)

fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("list 3 - 5 : ", fruitlist[2:5]) # sub list
print("start from 5 : ", fruitlist[4:]) # start from 5
print("end to 5 : ", fruitlist[:5]) # end to 5


# append and insert

fruitlist.append("firemelon") # append behave like push
print(fruitlist)

fruitlist.insert(3, alist) # insert
print(fruitlist)
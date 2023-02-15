# call me if you want to restore the file
def restoreFileContent():
    f = open("./file_handling/hello.txt", "w")
    f.write("hello world\nthis file is accessible through the following python code\nLorem ipsum dolor sit\namet, consectet\nmy name is lorem, everyone call me this name")
    f.close()

f = open("./file_handling/hello.txt") # by default is read text or rt

# check how many lines
lines = 0
for character in f :
    lines += 1
    print(character)
print(lines)

# close the file
f.close()

def getToReadFile() :
    return open("./file_handling/hello.txt", "r")

f = getToReadFile()

# read all lines in file
print(f.read())

f = getToReadFile()

# read per lines
print(f.readline())

f = getToReadFile()

# loop through line
for line in f :
    print(line)

# append a text to the end of the file
f = open("./file_handling/hello.txt", "a") # a mean append
f.write("hello to those who learn the python as programming language")
f.close()

f = getToReadFile()
print(f.read())

# write a text to the file
f = open("./file_handling/hello.txt", "w") # w mean write but also replace all its file contents
f.write("hello warudo")
f.close()

f = getToReadFile()
print(f.read())

# create a file
# call this function to create a new file
def createNewEmptyTXTFile(filename) :
    f = open(f"./file_handling/{filename}.txt", "x") # this line enough to create the empty file

f = open("./file_handling/hello.txt", "r")
print(f.read())

# delete a file
import os # import this module to delete a file

# call this function to delete a specific file
def deleteFile(filename):
    # check if file exists
    if os.path.exists(f"./file_handling/{filename}.txt"):
        os.remove(f"./file_handling/{filename}.txt")
    else: print("file does not exist")

# you can also delete a folder
def deleteFolder(foldername):
    os.rmdir(foldername)

# now try to delete test folder
    


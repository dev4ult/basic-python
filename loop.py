# while loop
i = 0
while i < 10:
    print(i)
    if i == 5:
        break # break out of while loop
    i += 1

# while loop with else
i = 0
while i < 10:
    print(i)
    i+= 1
else:
    print("i now is greather than 10")

# for loop
for i in range(10):
    print(i)

# for loop with array
for i in [2, 1, 5, 10]:
    if i == 1 :
        continue # jump over index
    print(i)
    
# find the smallest number of array in for loop
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15, 2]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)


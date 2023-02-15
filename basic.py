# casting
strtoint = int("123")
inttofloat = float(123)
floattostr = str(12.3)

print("casting : ", strtoint, " ", inttofloat, " ", floattostr)


# type
temp = "5 degrees"
cel = 0
print("type : ", type(temp))

# try catch exception
try:
    fahr = float(temp)
except ValueError:
    fahr = 0
cel = (fahr - 32.0) * 5.0 / 9.0
print("try catch : ", cel)

# multiple variable assignments
x, y, z = "Orange", "Banana", "Cherry"
print("Multiple variable assignment : ", x, y, z)

# about string
s = "Hello World"
print("about string : ", s, len(s), s[0], s[-1])

word = "banana"
i = word.find("na")
print(i)

# object point
a = 1
b = a
print("Check boolean", 0 == 0.0, 0 != 0.0, a is b)


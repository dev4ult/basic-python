
# type
temp = "5 degrees"
cel = 0
print(type(temp))

# try catch the exception
try:
    fahr = float(temp)
except ValueError:
    fahr = 0
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

# multiple variable assignments
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# object point
a = 1
b = a
print(0 == 0.0, 0 != 0.0, a is b)



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

# function
def hello():
    print("Hello World")

hello()

# function with parameters
def greet(name):
    print(f"Hello {name}")

greet("John")

# function with return
def greet_return(name):
    return f"Hello {name}"

hello_john = greet_return("John")
print(hello_john)

# function take a global variable
name = "global"
def hello_global():
    print(f"Hello {name}")

hello_global()
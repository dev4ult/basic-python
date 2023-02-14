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

# lambda
sayHello = lambda world : "hello " + world
print(sayHello("World"))

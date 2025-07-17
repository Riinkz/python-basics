def hello_world():
    print("Hello, World!")
    

hello_world()


def greeting(first_name, last_name):                # must use both arguments
    print(f"Hello, {first_name} {last_name}!")
    

greeting("John", "Doe")


# There are 2 different kind of functions:
# 1. Functions that return a value
# 2. Functions that perform a task

def get_greeting(name):
    return f"Hi {name}"


message =  get_greeting("John")
print(message)



def decrement(number, by):
    return number - by

# Long call
result = decrement(5, 2)
print(result)

# Short call
print(decrement(10, 4))

# Can also be written as
print(decrement(6, by=2))


# Default arguments
def decrement(number, by=1):
    return number - by
print(decrement(10))



# Variabel number of arguments
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5))
# 1. Write a function called cube() with one number parameter and returns the value of that number raised to the third power. Test the
# function by displaying the result of calling your cube() function on a few different numbers.
def cube(x):
    third_power = x ** -3
    return third_power

print(cube(3))

# 2. Write a function called greet() that takes one string parameter
# called name and displays the text "Hello <name>!", where <name> is replaced with the value of the name parameter.
def greet(name):
    print(f"Hello, {name}!")

print(greet("AJ"))
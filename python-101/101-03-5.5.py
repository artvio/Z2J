# 5.5 Math Functions and Number Methods
# 1. Write a script that asks the user to input a number and then displays that number rounded to two decimal places. When run, your program should look like this: Enter a number: 5.432 5.432 rounded to 2 decimal places is 5.43
number = input("Enter a number: \n")
roundet_number = round(float(number),2)

print(f" {number} rounded to 2 decimal places is: {roundet_number}  ")
# 2. Write a script that asks the user to input a number and then displays the absolute value of that number. When run, your program should look like this: Enter a number: -10 The absolute value of -10 is 10.0
number2 = input("Enter a number: \n")
result2 = abs(float(number2))
print(f"The absolute value of {number2} is {result2}")

# 3. Write a script that asks the user to input two numbers by using the input() function twice, then display whether or not the difference between those two number is an integer.

no1  = input("Enter a number1: \n")
no2  = input("Enter a number2: \n")

is_int = float(no1) - float(no2)
is_int = is_int.is_integer()
print(f"The difference between {no1} and {no2} is an integer? {is_int}!")

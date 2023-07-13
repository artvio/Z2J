# 5.2 Arithmetic Operators and Expressions
# Write a script called exponent.py that receives two numbers from the
# user and displays the first number raised to the power of the second number.

input1 = input("podaj liczbę:\n")
input2 = input("podaj potęgę:\n")

number1 = int(input1)
number2 = int(input2)

result = number1 ** number2

print(f"{number1} do potęgi {number2} = {result}")
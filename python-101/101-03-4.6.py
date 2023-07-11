# 1. Create a string containing an integer, then convert that string into an actual integer object using int(). Test that your new object is a number by multiplying it by another number and displaying the result.
strring = "1"
strring = int(strring)
print(strring * 4)

# 2. Repeat the previous exercise, but use a floating-point number and float().
strring2 = "1.2"
strring2 = float(strring2)
print(strring2 * 4)
# 3. Create a string object and an integer object, then display them side by side with a single print statement by using the str() function.

sttring3 = "string"
intt =  12
print(sttring3, str(intt))

# 4. Write a script that gets two numbers from the user using the input() function twice, multiplies the numbers together, and displays the result. If the user enters 2 and 4, your program should print the following text: The product of 2 and 4 is 8.0.
inp1 = input("podaj 1 liczbę \n")
inp2 = input("podaj 2 liczbę \n")

sum = float(inp1) * float(inp2)
print(sum)

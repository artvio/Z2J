# 1. Write a script that takes input from the user and displays that in- put back.
# 2. Writeascriptthattakesinputfromtheuseranddisplaystheinput in lowercase.
# 3. Writeascriptthattakesinputfromtheuseranddisplaysthenum- ber of characters inputted.

prompt = "Napisz coś 1: "
user_input = input (prompt)
print ("Napisałeś:", user_input)

prompt = "Napisz coś 2: "
user_input = input (prompt)
print ("Napisałeś:", user_input.lower(), ", ale zmieniłem litery na małe")

prompt = "Napisz coś 3: "
user_input = input (prompt)
len_user_input = len(user_input)
print ("Napisałeś:", len_user_input, "znaków")

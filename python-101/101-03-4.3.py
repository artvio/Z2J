# 1. Write a script that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honeybadger". Print each lowercase string on a separate line.
string1 = "Animals"
string2 = "Badger"
string3 = "Honey Bee"
string4 = "Honeybadger"

lowercase_string1 = string1.lower()
lowercase_string2 = string2.lower()
lowercase_string3 = string3.lower()
lowercase_string4 = string4.lower()

print(lowercase_string1)
print(lowercase_string2)
print(lowercase_string3)
print(lowercase_string4)

# 2. Repeat Exercise 1, but convert each string to uppercase instead of lowercase.
uppercase_string1 = string1.upper()
uppercase_string2 = string2.upper()
uppercase_string3 = string3.upper()
uppercase_string4 = string4.upper()

print(uppercase_string1)
print(uppercase_string2)
print(uppercase_string3)
print(uppercase_string4)

# 3. Write a script that removes whitespace from the following strings:
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
# Print out the strings with the whitespace removed.
print(string1.strip())
print(string2.strip())
print(string3.strip())

# 4. Write a script that prints out the result of .startswith("be") on each of the following strings:
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

# 5. Using the same four strings from Exercise 4, write a script that uses string methods to alter each string so that .startswith("be") returns True for all of them.
string1.strip()
string2.strip()
string3.strip()
string4.strip()

string1.lower()
string2.lower()
string3.lower()
string4.lower()

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

# Convert all strings to lowercase
string1 = string1.lower()
string2 = string2.lower()
string3 = string3.lower()
string4 = string4.lower().strip()  # Also remove leading spaces

# Check if each string starts with "be"
print(string1.startswith("be"))  # True
print(string2.startswith("be"))  # True
print(string3.startswith("be"))  # True
print(string4.startswith("be"))  # True
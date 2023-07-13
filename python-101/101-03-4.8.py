# 4.8 Find a String in a String
# 1. In one line of code, display the result of trying to .find() the substring "a" in the string "AAA". The result should be -1.
phrase = "AAA"
print(phrase.find("a"))

# 2. Replace every occurrence of the character "s" with "x" in the string "Somebody said something to Samantha.".
text = "Somebody said something to Samantha."
text = text.replace("s", "x")
print(text)
# 3. Write and test a script that accepts user input using the input() function and displays the result of trying to .find() a particular letter in that input.

user_input = input("Napisz coś \n")
print(user_input.find("a"))
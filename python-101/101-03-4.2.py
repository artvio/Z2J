# Concatenation, Indexing, and Slicing
# String Concatenation
string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
print(magic_string)

first_name = "Arthur"
last_name = "Dent"
full_name = first_name + " " + last_name
print(full_name)

# String Indexing
flavor = "apple pie"
print(flavor[1]) # p

# String Slicing
first_three_letters = flavor[0] + flavor[1] + flavor[2]
print(first_three_letters) # app

print(flavor[0:3]) # app
print(flavor[:5]) # apple
print(flavor[:]) # apple pie
print(flavor[:14]) # apple pie
print(flavor[13:15]) # ""
print(flavor[-9:-6]) # app
print(flavor[-9:0]) # ""

word = "goal"
word = "f" + word[1:]
print(word) # foal

# 1. Create a string and print its length using the len() function.
string = "string"
string = len(string)
print(string) #6

# 2. Create two strings, concatenate them, and print the resulting string.
string1 = "hello "
string2 = "world"
string3 = string1 + string2
print(string3) # hello world

# 3. Create two strings and use concatenation to add a space inbetween them. Then print the result.
string11 = "hello"
string22 = "world"
string33 = string11 + " " + string22
print(string3) # hello world
# 4. Print the string "zing" by using slice notation on the string "bazinga" to specify the correct range of characters.
string111 = "bazinga"
print(string111[2:6]) #zing


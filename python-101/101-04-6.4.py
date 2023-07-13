#6.4 Run in Circles

# 1. Write a for loop that prints out the integers 2 through 10, each on  a new line, by using the range() function.
for i in range(2,11):
    print(i)

# 2. Use a while loop that prints out the integers 2 through 10 (Hint: You’ll need to create a new integer first.)
int1 = 2
while int1 < 11:
    print(int1)
    int1 += 1

# 3. Write a function called doubles() that takes one number as its input
# and doubles that number. Then use the doubles() function in a loop to double the number 2 three times, displaying each result on a separate line.

def doubles(number):
    double = number * number
    return double

for i in range(3):
    print(doubles(i))

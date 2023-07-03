"""X == Y # sprawdzenie czy X równa się Y
X != Y # sprawdzenie czy X jest różne od Y
X > Y
X < Y
X >= Y
X <= Y"""

x = 5
y = 3

print("Porównania arytmetyczne:")
print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x > y:", x > y)  # True
print("x < y:", x < y)  # False
print("x >= y:", x >= y)  # True
print("x <= y:", x <= y)  # True

print("Porównania logiczne:")
print("x == y and x < 10:", x == y and x < 10)  # False
print("x > y or y > 0:", x > y or y > 0)  # True
print("not(x == y):", not(x == y))  # True

print()
x = 5
print(x < 5 and x < 10)
x = 5
print(x > 3 and x < 10)
print(not(x > 3 and x < 10))

print("------")
print(not(x > 3 and x < 10))

print(not x > 3 and x < 10)

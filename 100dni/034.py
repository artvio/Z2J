this_list = ["apple", "banana", "cherry"]

print(this_list)
this_list.append("orange")
print(this_list)

print("------------------")
this_list = ["apple", "banana", "cherry"]

print(this_list)
this_list.insert(0, "pineapple")
print(this_list)
print("------------------")
fruits = ["apple", "banana", "cherry"]
tropical_fruits = ["mango", "pineapple", "papaya"]
fruits.extend(tropical_fruits)
print(fruits)
print("------------------")

fruits = ["apple", "banana", "cherry"]
print("Lista startowa: ", fruits)

fruits.remove("banana")
print("remove: ", fruits)

#pop wersja z argumentem
fruits = ["apple", "banana", "cherry"]
fruits.pop(0)
print("pop(0): ", fruits)

#pop wersja bez agrumentu
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print("pop(): ", fruits)

# clear
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print("clear(): ", fruits)
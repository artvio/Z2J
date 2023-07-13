# 4.7 Streamline Your Print Statements
# 1. Create a float object named weight with the value 0.2, and create a string object named animal with the value "newt". Then use these objects to print the following string using only string concatenation: 0.2 kg is the weight of the newt.
weight = 0.2
animal = "newt"
result = str(weight) + " kg is the weight of the " + animal + "."
print(result)

# 2. Display the same string by using the .format() method and empty {} place-holders.
weight = 0.2
animal = "newt"
result = "{} kg is the weight of the {}.".format(weight, animal)
print(result)

# 3. Display the same string using an f-string.
print(f"{weight} kg is the weight of the {animal}")
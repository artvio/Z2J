# 6.3 Challenge: Convert Temperatures

# 1. convert_cel_to_far() which takes one float parameter representing
# degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula:
# F = C * 9/5 + 32
def convert_cel_to_far(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def convert_far_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit_input = float(input("Enter a temperature in degrees Fahrenheit: "))
celsius_output = convert_far_to_cel(fahrenheit_input)
rounded_celsius_output = round(celsius_output, 2)
print("The temperature in degrees Celsius is:", rounded_celsius_output)

celsius_input = float(input("Enter a temperature in degrees Celsius: "))
fahrenheit_output = convert_cel_to_far(celsius_input)
rounded_fahrenheit_output = round(fahrenheit_output, 2)
print("The temperature in degrees Fahrenheit is:", rounded_fahrenheit_output)
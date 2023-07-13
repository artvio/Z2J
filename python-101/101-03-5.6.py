# 5.6 Print Numbers in Style
# 1. Print the result of the calculation 3 ** .125 as a fixed-point number with three decimal places.
# 2. Print the number 150000 as currency, with the thousands grouped with commas. Currency should be displayed with two decimal places.
# 3. Print the result of 2 / 10 as a percentage with no decimal places. The output should look like 20%.

no = 3 ** 0.125
print(no)
print(f"Over {no:.3f} of Pythonistas say 'Real Python rocks!'")

money = 150000
print(f"Money: {money:,.2f} ")

result = 2 / 10
formatted_result = f"{result:.0%}"
print(formatted_result)
# 6.5 Challenge: Track Your Investments
# In this challenge, you will write a program called invest.py that tracks
# the growing amount of an investment over time.
# An initial deposit, called the principal amount, is made. Each year,
# the amount increases by a fixed percentage, called the annual rate of
# return.
# For example, a principal amount of $100 with an annual rate of return
# of 5% increases the first year by $5. The second year, the increase is
# 5% of the new amount $105, which is $5.25.
# Write a function called invest with three parameters: the principal
# amount, the annual rate of return, and the number of years to calculate. The function signature might look something like this:
# def invest(amount, rate, years):
# The function then prints out the amount of the investment, rounded
# to 2 decimal places, at the end of each year for the specified number  of years.

# To finish the program, prompt the user to enter an initial amount, an
# annual percentage rate, and a number of years. Then call invest() to display the calculations for the values entered by the user.

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f'year {year}: ${amount:.2f}')

def main():
    amount = float(input("Enter the initial amount: "))
    rate = float(input("Enter the annual rate of return: "))
    years = int(input("Enter the number of years: "))
    invest(amount, rate, years)

if __name__ == "__main__":
    main()
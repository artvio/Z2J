wiek = input("Podaj swój wiek\n")
wiek_liczba = int(wiek)  # wiek pobrany jako liczba


if wiek_liczba >= 18:
    print("Pełnoletni")
else:
    print("Niełnoletni")

for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")
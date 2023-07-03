owoce = ["jabłko", "banan", "wiśnia"]
print(owoce)

print(owoce[0]) #wypisze "jabłko"
print(owoce[1]) #wypisze "banan"

owoce[0] = "gruszka"
print(owoce) #wypisze ["gruszka", "banan", "wiśnia"]

"""
Zadanie na dzisiaj:

1) Utwórz listę z pięcioma swoimi ulubionymi owocami.
2) Wypisz na ekranie drugi owoc z listy.
3) Zmień trzeci owoc na coś innego.
4) Wypisz na ekranie pierwszy i trzeci owoc z listy.
"""
owoce = ["jabłko", "banan", "wiśnia", "kiwi", "porzeczka"]
print(owoce)
print(owoce[1])
owoce[2] = "winogrono"
print(owoce[0], owoce[2])

napoje = ['cola', 'sok pomarańczowy', 'woda', 'kawa']

if len(napoje[0]) < 10:
    print("Ta nazwa jest krótka")
else:
    print("Ta nazwa jest długa")
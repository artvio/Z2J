while True:
    weight = input("Podaj wagę (kg) np. 75:\n")
    try:
        weight = float(weight)
        break
    except ValueError:
        print("Błędne dane. Wprowadź liczbę.")

while True:
    height = input("Podaj (m) np. 1.75\n")
    try:
        height = float(height)
        break
    except ValueError:
        print("Błędne dane. Wprowadź liczbę.")

bmi = weight / (height * height)

def interpretuj_bmi(bmi):
    if bmi < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi <= 24.9:
        return "Waga prawidłowa"
    elif 25 <= bmi <= 29.9:
        return "Nadwaga"
    elif 30 <= bmi <= 34.9:
        return "Otyłość (klasa I)"
    elif 35 <= bmi <= 39.9:
        return "Otyłość (klasa II)"
    else:
        return "Otyłość (klasa III)"
komunikat = interpretuj_bmi(bmi)

print("Twoje BMI wynosi: " + str(bmi))
print(str(komunikat))
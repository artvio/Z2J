dlugiCiagZnakow = "Nauka Python jest super"
print(len(dlugiCiagZnakow))  # 23
print(dlugiCiagZnakow[6:12])  # Python
print(dlugiCiagZnakow[6:])  # Python jest super
print(dlugiCiagZnakow[:6])  # Nauka
print(dlugiCiagZnakow[-10:-2])  # jest sup

nazwaBloga = "Zero To Junior"
print(nazwaBloga.upper())  # ZERO TO JUNIOR
print(nazwaBloga.lower())  # zero to junior
print(nazwaBloga.startswith("Junior"))  # False
print(nazwaBloga.endswith("Junior"))  # True
print(nazwaBloga.count("o"))  # 3

nazwaBloga = "Zero To Junior"
liczba = "12345678"

print(nazwaBloga.swapcase())  # zERO tO jUNIOR Zamienia duże litery na małe i małe litery na duże.
print(nazwaBloga.replace(" ", "_"))  # Zero_To_Junior Zamienia spacje na podkreślenia.
print(nazwaBloga.isdigit())  # False Sprawdza, czy łańcuch składa się tylko z cyfr.
print(nazwaBloga.isalpha())  # False Sprawdza, czy łańcuch składa się tylko z liter.
print(liczba.isdigit())  # True sprawdza, czy łańcuch składa się tylko z cyfr.
print(liczba.isalpha())  # False Sprawdza, czy łańcuch składa się tylko z liter.

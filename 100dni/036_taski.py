zadania = ['Zadanie A', 'Zadanie B', 'Zadanie C', 'Zadanie D', 'Zadanie E']
dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek']

liczba_tygodni = 3
liczba_zadan = len(zadania)

for tydzien in range(liczba_tygodni):
    for dzien in range(5):
        numer_zadania = dzien + 1
        opis_zadania = zadania[dzien]
        print(f"{tydzien+1} - {numer_zadania} - {opis_zadania}")


tasks = ['ZA', 'ZB', 'ZC', 'ZD', 'ZE']

for i in range(1, 22):
    for x in range(1, 6):
        print(i, x, tasks[x - 1])



pustaLista1 = []
pustaLista2 = list()

pelnaLista1 = [1, 4, 6, 10]
pelnalista2 = list([1, 4, 6, 10])

print(pustaLista1)
print(pustaLista2)
print(pelnaLista1)
print(pelnalista2)

"""Range
Poznaj range. Metodę, która generuje sekwencję liczb, kolejnych i niepowtarzalnych.
# Składnia
range(start, stop, step)
# start (opcjonalnie) - mówi od której wartości zaczynamy.
# stop (wymagane) - do której wartości należy doliczyć
# step (opcjonalne) - jeśli ustalimy ten parametr to będziemy przesuwać się o więcej niż jedna wartość. Wartość domyślna to 1.
"""
print(range(10))


# możemy napisać tak:
# print(list(range(10)))
# ale dla Twojej wygody, zrobimy to czytelniej

liczby = range(10)
lista_liczb = list(liczby)
print(lista_liczb)

print("liczby - ", liczby)


x = list(range(3, 10))
y = list(range(0, 10, 3))
z = list(range(0, -10, -1))

print(x, y, z)
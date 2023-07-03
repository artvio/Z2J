# Zadanie ekstra dodatkowe:
# Napisz własną funkcję maximum(),
# która znajduje największą liczbę,
# nie używając gotowej komendy max().

numbers1 = [1,3,6,12,1,23,43,12,11]
def maximum(numbers):
    max_value = numbers[0]  # Przyjmujemy pierwszą liczbę jako aktualnie maksymalną

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value


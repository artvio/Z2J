numbers1 = [1,3,6,12,1,23,43,12,11]
numbers2 = [1,3,6,12,1,23,43,12,12]
numbers3 = [1,3,6,12,1,23,43,12,13]
def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg


print(average(numbers1))
print(average(numbers2))

avg3 = average(numbers3)
print(avg3)

print("------------")
liczby = [1,2,3]
def printavg(value):
    total = sum(value)
    count = len(value)
    avg = total / count
    return avg

avg = printavg(liczby)
print("Średnia wynosi ",avg)

print("------------")
def printavg(value):
    total = sum(value)
    avg = total / len(value)
    print("Średnia wynosi:", avg)

liczby = [1, 2, 3, 4]
printavg(liczby)
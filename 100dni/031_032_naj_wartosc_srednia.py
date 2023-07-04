numbers1 = [1, 3, 6, 12, 1, 23, 43, 12, 11, 100]
numbers2 = [1, 3, 6, 12, 1, 23, 43, 12, 12, 200]
numbers3 = [1, 3, 6, 12, 1, 23, 43, 12, 13, 300]

numbers = [numbers1, numbers2, numbers3]
print (numbers)
def print_avg(value):
    print("Średnia wynosi:", value)

def find_max(numbers):
    max_value = max(numbers)
    print("Największa wartość to:", max_value)

def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

for nums in numbers:
    avg = average(nums)
    max_value = find_max(nums)
    print_avg(avg)
    print()

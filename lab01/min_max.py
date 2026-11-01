from functools import reduce

numbers = [10, 20, 5, 30, 15]

min = reduce(lambda x, y: x if x < y else y, numbers)
max = reduce(lambda x, y: x if x > y else y, numbers)

print(f"Min: {min}, Max: {max}")

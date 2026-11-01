numbers = [1, 2, 3, 4, 5]

processed = map(lambda x: x**2, list(filter(lambda x: x % 2 != 0, numbers)))

print(list(processed))

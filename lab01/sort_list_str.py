animals = ["dog", "cat", "elephant", "bear", "zebra"]

sorted_animals = sorted(animals, key=lambda x: -len(x))

print(list(sorted_animals))

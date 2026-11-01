from functools import reduce

names = ["Alice", "Bob", "Charlie", "David"]

name_length_map = reduce(lambda x, y: {**x, y: len(y)}, names, {})

print(name_length_map)

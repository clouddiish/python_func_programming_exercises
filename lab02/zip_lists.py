from functools import reduce

keys = ["one", "two", "three"]
values = [1, 2, 3]

zipped = reduce(lambda acc, elem: {**acc, **elem}, map(lambda key, value: {key: value}, keys, values))

print(zipped)

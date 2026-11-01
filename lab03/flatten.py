from functools import reduce

list_of_lists = [["apple", "banana"], ["carrot", "daikon"], ["eggplant", "fig"]]

flattened_list = reduce(lambda acc, sublist: acc + sublist, list_of_lists, [])

print(flattened_list)

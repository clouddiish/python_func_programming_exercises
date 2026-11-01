from functools import reduce

numbers = [1, 2, 3, 2, 3, 4, 3, 5, 4, 6, 7, 3, 8, 3, 9]

frequency = reduce(lambda acc, number: {**acc, number: acc.get(number, 0) + 1}, numbers, {})
most_frequent = max(frequency.items(), key=lambda item: item[1])[0]

print("Most Frequent Element:", most_frequent)

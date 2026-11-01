from functools import reduce

words = ["java", "is", "cool", "but", "challenging"]

grouped_by_length = reduce(lambda acc, word: {**acc, len(word): acc.get(len(word), []) + [word]}, words, {})

print(grouped_by_length)

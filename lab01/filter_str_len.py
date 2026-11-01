phrases = ["apple", "pear", "banana", "grape", "strawberry"]

long_phrases = filter(lambda x: len(x) > 5, phrases)

print(list(long_phrases))

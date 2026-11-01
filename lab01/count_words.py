sentences = ["Hello world", "Functional programming in Java", "Stream API"]

word_counts = map(lambda x: len(x.split()), sentences)

print(list(word_counts))

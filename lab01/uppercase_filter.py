names = ["Alice", "Bob", "Alex", "Annie", "Brian"]

filtered_names = filter(lambda x: x[0] != "A", list(map(lambda x: x.upper(), names)))

print(list(filtered_names))

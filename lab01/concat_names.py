names = ["John", "Jane", "Mary", "Mike"]

result = "Names: " + ",".join(list(map(lambda x: x.upper(), names)))

print(result)

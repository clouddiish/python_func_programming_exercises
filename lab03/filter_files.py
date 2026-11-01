import os

files = os.listdir(".")

result = list(filter(lambda file: file.endswith(".py"), files))
print("\n".join(result))

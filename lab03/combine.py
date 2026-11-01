import os

files = list(filter(lambda entry: os.path.isfile(entry), os.listdir(".")))
sorted_uppercase = sorted(list(map(lambda filename: filename.upper(), files)))

print("\n".join(sorted_uppercase))

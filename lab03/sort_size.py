import os

files = list(filter(lambda entry: os.path.isfile(entry), os.listdir(".")))
sorted_by_size = sorted(files, key=lambda file: os.path.getsize(file))

for file in sorted_by_size:
    print(file, os.path.getsize(file), "bytes")

import os
from functools import reduce


def list_files_in_dir(dir):
    entries = os.listdir(dir)
    files = list(filter(lambda entry: os.path.isfile(os.path.join(dir, entry)), entries))
    subdirectories = list(filter(lambda entry: os.path.isdir(os.path.join(dir, entry)), entries))
    subdir_files = reduce(lambda acc, subdir: acc + list_files_in_dir(os.path.join(dir, subdir)), subdirectories, [])

    return files + subdir_files


flattened_files = list_files_in_dir("./")
print("\n".join(flattened_files))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sorted = sorted(list(filter(lambda x: x % 2 == 0, numbers)), reverse=True)

print(list(even_sorted))

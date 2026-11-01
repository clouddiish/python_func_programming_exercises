numbers = [1, 2, 3, 4, 5]


def double_numbers():
    for x in numbers:
        print(f"Doubling {x}")
        yield x * 2


list(map(print, double_numbers()))

from functools import reduce

words = ["Java", "Functional", "Programming", "Collector"]
separator = " "


def concatenating_collector(acc, word):
    if acc:
        acc.append(separator)
    acc.append(word.upper())
    return acc


result = "".join(reduce(concatenating_collector, words, []))

print(result)

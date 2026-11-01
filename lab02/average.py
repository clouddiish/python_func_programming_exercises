from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total_sum = reduce(lambda acc, number: acc + number, numbers, 0)
average = total_sum / len(numbers) if numbers else None

if average is not None:
    print("The average is:", average)
else:
    print("Could not calculate the average")

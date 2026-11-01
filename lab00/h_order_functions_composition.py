add_one = lambda x: x + 1
multiply_by_two = lambda x: x * 2

composed_function = lambda x: multiply_by_two(add_one(x))

result = composed_function(4)

print(f"Result: {result}")

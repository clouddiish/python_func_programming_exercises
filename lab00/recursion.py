def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(f"Factorial of 5: {result}")

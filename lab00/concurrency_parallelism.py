from concurrent.futures import ThreadPoolExecutor


def task1():
    print("Task 1 is executing")


def task2():
    print("Task 2 is executing")


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(task1)
    executor.submit(task2)

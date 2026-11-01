from functools import reduce


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def to_JSON(self):
        return f'{{"name": "{self.name}", "age": {self.age}}}'


def main() -> None:
    users = [User("Alice", 30), User("Bob", 25)]
    json = "[" + ",".join(list(map(lambda user: user.to_JSON(), users))) + "]"
    print(json)


if __name__ == "__main__":
    main()

from functools import reduce

from person import SAMPLE_DATA


def main() -> None:
    name_count = reduce(
        lambda acc, person: {**acc, person.last_name: acc.get(person.last_name, 0) + 1}, SAMPLE_DATA, {}
    )
    print(name_count)


if __name__ == "__main__":
    main()

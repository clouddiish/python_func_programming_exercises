from functools import reduce

from person import SAMPLE_DATA


def main() -> None:
    unique_first_names = reduce(
        lambda names, person: names + [person.first_name] if person.first_name not in names else names, SAMPLE_DATA, []
    )
    print(unique_first_names)


if __name__ == "__main__":
    main()

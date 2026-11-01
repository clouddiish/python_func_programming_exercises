from functools import reduce

from person import SAMPLE_DATA


def main() -> None:
    result = reduce(
        lambda acc, person: {
            **acc,
            person.last_name: acc.get(person.last_name, [])
            + list(filter(lambda num: num[0:2] == "+1", person.phone_numbers)),
        },
        SAMPLE_DATA,
        {},
    )
    print(result)


if __name__ == "__main__":
    main()

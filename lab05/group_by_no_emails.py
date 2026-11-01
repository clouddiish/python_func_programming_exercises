from functools import reduce

from person import SAMPLE_DATA


def main() -> None:
    people_by_email_count = reduce(
        lambda acc, person: {
            **acc,
            len(person.email_addresses): acc.get(len(person.email_addresses), []) + [person.full_name()],
        },
        SAMPLE_DATA,
        {},
    )
    print(people_by_email_count)


if __name__ == "__main__":
    main()

from functools import reduce

from person import SAMPLE_DATA


def main() -> None:
    max_emails_person = reduce(
        lambda current_max, person: (
            person if len(person.email_addresses) > len(current_max.email_addresses) else current_max
        ),
        SAMPLE_DATA,
        SAMPLE_DATA[0],
    )
    print(f"{max_emails_person.full_name()} has the most email addresses")


if __name__ == "__main__":
    main()

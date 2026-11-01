from functools import reduce

from person import SAMPLE_DATA


def main() -> None:
    emails = reduce(lambda emails, person: emails + person.email_addresses, SAMPLE_DATA, [])
    total_emails = reduce(lambda acc, email: acc + 1, emails, 0)
    print(f"Total number of email addresses: {total_emails}")


if __name__ == "__main__":
    main()

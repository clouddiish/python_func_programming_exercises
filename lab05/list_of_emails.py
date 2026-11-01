from functools import reduce

from person import SAMPLE_DATA


def main() -> None:
    all_email_adresses = reduce(lambda emails, person: emails + person.email_addresses, SAMPLE_DATA, [])
    print(all_email_adresses)


if __name__ == "__main__":
    main()

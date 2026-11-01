from dataclasses import dataclass
from functools import reduce

from person import Person, SAMPLE_DATA


@dataclass
class MinMax:
    youngest: Person
    oldest: Person


def main() -> None:
    result = reduce(
        lambda acc, person: MinMax(
            youngest=person if person.age < acc.youngest.age else acc.youngest,
            oldest=person if person.age > acc.oldest.age else acc.oldest,
        ),
        SAMPLE_DATA,
        MinMax(youngest=SAMPLE_DATA[0], oldest=SAMPLE_DATA[0]),
    )
    print(result)


if __name__ == "__main__":
    main()

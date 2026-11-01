from dataclasses import dataclass, field
from typing import List


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    email_addresses: List[str] = field(default_factory=list)
    phone_numbers: List[str] = field(default_factory=list)

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


# Sample data
SAMPLE_DATA: List[Person] = [
    Person(
        first_name="Alice",
        last_name="Johnson",
        age=25,
        email_addresses=["alice.johnson@example.com"],
        phone_numbers=["+123456789", "987654321"],
    ),
    Person(
        first_name="Bob",
        last_name="Smith",
        age=30,
        email_addresses=["bob.smith@example.com"],
        phone_numbers=["+1987654321", "876543210"],
    ),
    Person(
        first_name="Charlie",
        last_name="Johnson",
        age=35,
        email_addresses=["charlie.johnson@example.com"],
        phone_numbers=["+1123456789", "5432109876"],
    ),
]

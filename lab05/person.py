from dataclasses import dataclass, field
from typing import List


@dataclass
class Person:
    first_name: str
    last_name: str
    email_addresses: List[str] = field(default_factory=list)

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


# Sample data
SAMPLE_DATA: List[Person] = [
    Person("John", "Doe", []),
    Person("Sara", "Walker", ["sara@example.com"]),
    Person("Mike", "Baker", ["mike@example.com", "baker@example.com"]),
    Person("Dev", "Shah", ["dev@example.com", "shah@example.com"]),
    Person("Sara", "Lee", ["slee@example.org", "lee@example.com"]),
    Person("Nancy", "Xie", ["nancy@example.com", "xie@example.com", "nx@example.com"]),
    Person("Jill", "Smith", ["jill@example.com"]),
]

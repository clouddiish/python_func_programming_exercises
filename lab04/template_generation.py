from typing import Callable


def main() -> None:
    template = "Dear ${name},\n\nYour appointment is scheduled on ${date}.\n\nBest regards,\nYour Company"

    def replace_placeholder(t, placeholder):
        placeholder_name, placeholder_value = placeholder.split(":")
        placeholder = f"${{{placeholder_name}}}"
        return t.replace(placeholder, placeholder_value)

    email = replace_placeholder(template, "name:John Doe")
    email = replace_placeholder(email, "date: April 24, 2024")
    print(email)


if __name__ == "__main__":
    main()

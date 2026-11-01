def process(text: str, shift: int):
    shift %= 26

    def caesar_shift(ch: str) -> str:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            ch = chr((ord(ch) - base + shift + 26) % 26 + base)
        return ch

    return "".join(caesar_shift(c) for c in text)


def main() -> None:
    message = "Hello World!"
    encrypted = process(message, 3)
    decrypted = process(encrypted, -3)

    print("Original:  ", message)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)


if __name__ == "__main__":
    main()

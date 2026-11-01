from functools import reduce


def reverse_words(sentence: str) -> str:
    return " ".join(reduce(lambda acc, word: [word] + acc, sentence.split(), []))


def main() -> None:
    sentence = "Hello world, this is a test"
    print("Original:", sentence)
    print("Reversed:", reverse_words(sentence))


if __name__ == "__main__":
    main()

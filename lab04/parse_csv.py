from pathlib import Path
import traceback


def main() -> None:
    path = Path("data.csv")
    try:
        with path.open(encoding="utf-8") as file:
            list(map(lambda fields: print(fields[0], fields[1]), map(lambda line: line.split(","), file)))
    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    main()

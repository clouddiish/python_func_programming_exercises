from dataclasses import dataclass
from typing import Callable


@dataclass
class Color:
    r: int
    g: int
    b: int


class Camera:
    def __init__(self) -> None:
        self.filter: Callable[[Color], Color] = lambda c: c

    def set_filter(self, filter_func: Callable[[Color], Color]) -> None:
        self.filter = filter_func

    def capture(self, input_color) -> Color:
        return self.filter(input_color)


def main() -> None:
    camera = Camera()
    camera.set_filter(
        lambda c: Color(r=min(int(c.r * 1.1), 255), g=min(int(c.g * 1.1), 255), b=min(int(c.b * 1.1), 255))
    )
    result = camera.capture(Color(r=200, g=100, b=200))
    print(f"Captured color with brighter filter: {result}")


if __name__ == "__main__":
    main()

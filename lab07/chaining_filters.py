from dataclasses import dataclass
from functools import reduce
from typing import Callable


@dataclass
class Color:
    r: int
    g: int
    b: int


class Camera:
    def __init__(self):
        self.filter: Callable[[Color], Color] = lambda c: c

    def set_filters(self, *filters: Callable[[Color], Color]):
        self.filter = reduce(lambda acc, f: lambda color: f(acc(color)), filters, lambda color: color)

    def capture(self, input_color):
        return self.filter(input_color)


def main() -> None:
    camera = Camera()
    camera.set_filters(
        lambda c: Color(r=min(int(c.r * 1.1), 255), g=min(int(c.g * 1.1), 255), b=min(int(c.b * 1.1), 255)),
        lambda c: Color(r=max(int(c.r * 0.9), 0), g=max(int(c.g * 0.9), 0), b=max(int(c.b * 0.9), 0)),
    )
    result = camera.capture(Color(r=200, g=100, b=200))
    print(f"Captured color with brighter & darker filters: {result}")


if __name__ == "__main__":
    main()

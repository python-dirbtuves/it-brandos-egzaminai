from pathlib import Path
from typing import List, Tuple, Iterator


class Rover(object):
    BRAIN = {
        1: (0, 1),
        2: (1, 0),
        3: (0, -1),
        4: (-1, 0),
    }

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.reset(x, y)

    def reset(self, x: int, y: int) -> None:
        self.x, self.y = x, y

    def has_arrived(self, x: int, y: int) -> bool:
        return self.x == x and self.y == y

    def move(self, command: int) -> None:
        x, y = self.BRAIN[command]
        self.x += x
        self.y += y

    def walk_to(self, x: int, y: int, n: int, *commands: int) -> Tuple[bool, Tuple[int, ...]]:
        """Executes commands and returns if x, y destination is reached."""
        for i, command in enumerate(commands[:n], 1):
            self.move(command)
            if self.has_arrived(x, y):
                return True, commands[:i]
        return False, commands


def read_ints(lines: Iterator[str]) -> Iterator[int]:
    return map(int, next(lines).split())


def consume_data(lines: Iterator[str], rover: Rover) -> Iterator[Tuple[bool, Tuple[int, ...]]]:
    # Get initial position.
    x0, y0 = read_ints(lines)

    # Get destination.
    x1, y1 = read_ints(lines)

    # Get number of commands to execute.
    n, = read_ints(lines)

    # Send commands to rover.
    for i in range(n):
        rover.reset(x0, y0)
        yield rover.walk_to(x1, y1, *read_ints(lines))


def format_results(results: List[Tuple[bool, Tuple[int, ...]]]) -> Iterator[str]:
    for found, path in results:
        message = "pasiektas tikslas" if found else "sekos pabaiga"
        yield '%-20s %s %s' % (message, ' '.join(map(str, path)), len(path))


def main(path: Path) -> None:
    # Read and process input data.
    with open(path / 'U2.txt') as f:
        results = list(consume_data(f, Rover()))

    # Write results to output file.
    with open(path / 'U2rez.txt', 'w') as f:
        for line in format_results(results):
            print(line, file=f)

from pathlib import Path
from typing import List, Tuple, Iterator, Dict, Any


def read_ints(lines: Iterator[str]) -> List[int]:
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def move(brain: Dict[int, Tuple[int, int]], step: int, x: int, y: int) -> Tuple[int, int]:
    """Calculate next position."""
    xd, yd = brain[step]
    return x + xd, y + yd


def walk(brain: Dict[int, Tuple[int, int]], steps: List[int], x0: int, y0: int) -> List[Any]:
    """Execute given steps and return data about how it went."""
    ret: List[Any] = []
    done = []
    x, y = x0, y0
    for step in steps:
        done.append(step)
        x, y = move(brain, step, x, y)
        if (x, y) == (x0, y0):
            return ret + ['%-20s' % 'pasiektas tikslas'] + done + [len(done)]
    return ret + ['%-20s' % 'sekos pabaiga'] + done + [len(done)] + [x, y]


def read_lines(brain: Dict[int, Tuple[int, int]], lines: Iterator[str]) -> Iterator[List[Any]]:
    x0, y0 = read_ints(lines)
    n, = read_ints(lines)
    for i in range(n):
        k, *steps = read_ints(lines)
        steps = steps[:k]
        yield walk(brain, steps[:k], x0, y0)


def main(path: Path) -> None:
    brain = {
        1: (1, 1),
        2: (1, -1),
        3: (-1, -1),
        4: (-1, 1),
    }

    with open(path / 'U2rez.txt', 'w') as fout, open(path / 'U2.txt') as fin:
        for line in read_lines(brain, fin):
            print(*line, file=fout)


if __name__ == '__main__':
    main(Path())

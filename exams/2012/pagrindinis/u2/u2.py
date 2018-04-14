#!/usr/bin/env python3

from pathlib import Path
from typing import List, Tuple, Iterator


def parse_ints(line: str) -> List[int]:
    return list(map(int, line.split()))


def read_row(lines: Iterator[str], k: int) -> Tuple[str, List[int]]:
    line = next(lines)
    name = line[:10]
    points = parse_ints(line[10:])
    return name, points[:k]


def get_points(points: List[int]) -> int:
    return sum([p if p % 2 == 0 else -p for p in points])


def get_even_points(points: List[int]) -> int:
    return sum([p for p in points if p % 2 == 0])


def read_data(lines: Iterator[str]) -> Iterator[Tuple[int, int, str]]:
    n, k = parse_ints(next(lines))
    for i in range(n):
        name, points = read_row(lines, k)
        yield -get_points(points), -get_even_points(points), name


def main(path: Path) -> None:
    with open(path / 'U2.txt') as f:
        result = sorted(read_data(f))

    with open(path / 'U2rez.txt', 'w') as f:
        points, _, name = result[0]
        print('%s%s' % (name, -points), file=f)


if __name__ == '__main__':
    main(Path())

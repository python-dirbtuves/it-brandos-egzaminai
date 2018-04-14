from itertools import islice
from pathlib import Path
from typing import List, Tuple, Iterator, Optional, NamedTuple


class Company(NamedTuple):
    name: str
    x: int
    y: int


def read_data(lines: Iterator[str], n: int) -> Iterator[Company]:
    for line in islice(lines, n):
        company, x, y = line.strip().split()
        yield Company(company, int(x), int(y))


def get_distance(x: int, y: int) -> int:
    return (abs(x) + abs(y)) * 2


def simulate_single_day(data: Iterator[Company], m: int) -> Tuple[int, int, str]:
    distance = 0
    result = (0, distance, '')
    for i, (company, x, y) in enumerate(data, 1):
        distance += get_distance(x, y)
        if distance >= m:
            break
        result = (i, distance, company)
    return result


def main(path: Path) -> None:
    with open(path / 'U1.txt') as f:
        n, m = map(int, next(f).split())
        data = read_data(f, n)
        result = simulate_single_day(data, m)

    with open(path / 'U1rez.txt', 'w') as f:
        print(*result, file=f)

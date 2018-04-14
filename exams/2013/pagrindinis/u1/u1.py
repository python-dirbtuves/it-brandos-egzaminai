#!/usr/bin/env python3

from pathlib import Path
from typing import List, Tuple, Iterator, Optional


def read_ints(lines: Iterator[str]) -> List[int]:
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def read_row(lines: Iterator[str]) -> Tuple[str, int, int]:
    line = next(lines)
    company = line[:10].strip()
    x, y = line[10:].split()
    return company, int(x), int(y)


# užduotyje reikalauja atskiros funkcijos
def way_to_company(x: int, y: int) -> int:
    return (abs(x) + abs(y)) * 2


def simulate_single_day(lines: Iterator[str], n: int, m: int) -> Tuple[int, int, Optional[str]]:
    distance = 0
    result: Tuple[int, int, Optional[str]] = (0, distance, None)
    for i in range(n):
        company, x, y = read_row(lines)
        distance += way_to_company(x, y)
        if distance >= m:
            return result
        result = (i+1, distance, company)
    return result


def main(path: Path) -> None:
    with open(path / 'U1.txt') as f:
        n, m = read_ints(f)
        result = simulate_single_day(f, n, m)

    with open(path / 'U1rez.txt', 'w') as f:
        print(*result, file=f)


if __name__ == '__main__':
    main(Path())

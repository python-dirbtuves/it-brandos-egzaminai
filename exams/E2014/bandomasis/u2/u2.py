from collections import defaultdict
from operator import itemgetter
from pathlib import Path
from typing import List, Tuple, Iterator, Dict


def read_row(lines: Iterator[str]) -> Tuple[str, int, str]:
    line1 = next(lines)
    line2 = next(lines)
    return line1[:20].strip(), int(line1[20:]), line2[:13].strip()


def read_data(lines: Iterator[str], k: int) -> Dict[str, Dict[str, int]]:
    data: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for i in range(k):
        municipality, n_schools, district = read_row(lines)
        max_n_schools = max(data[district][municipality], n_schools)
        data[district][municipality] = max_n_schools
    return data


def calculate_stats(data: Dict[str, Dict[str, int]]) -> List[Tuple[str, int, int]]:
    stats = [
        (district, len(municipalities), max(municipalities.values()))
        for district, municipalities in data.items()
    ]
    stats.sort(key=itemgetter(0))
    stats.sort(key=itemgetter(2), reverse=True)
    return stats


def main(path: Path) -> None:
    with open(path / 'U2.txt') as f:
        k = int(next(f).strip())
        data = read_data(f, k)
        stats = calculate_stats(data)

    with open(path / 'U2rez.txt', 'w') as f:
        print(len(data), file=f)
        for row in stats:
            print('%-13s %d %d' % row, file=f)

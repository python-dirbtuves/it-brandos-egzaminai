import sys
import operator
import collections
from pathlib import Path
from typing import List, Tuple, Iterator, Optional, Dict


class Record(object):
    def __init__(self, district: Optional[str]=None, smallest: int=sys.maxsize, total: int=0) -> None:
        self.district = district
        self.smallest = smallest
        self.total = total


def read_ints(lines: Iterator[str]) -> List[int]:
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def read_row(lines: Iterator[str]) -> Tuple[str, str, int]:
    line = next(lines)
    city = line[:20].strip()
    district = line[20:33].strip()
    n = int(line[33:])
    return city, district, n


def main(path: Path) -> None:
    with open(path / 'U2.txt') as f:
        k, = read_ints(f)
        result: Dict[str, Record] = collections.defaultdict(Record)
        for i in range(k):
            city, district, population = read_row(f)
            record = result[district]
            record.district = district
            record.smallest = min(record.smallest, population)
            record.total += population

    with open(path / 'U2rez.txt', 'w') as f:
        print(len(result), file=f)
        sort_key = operator.attrgetter('smallest', 'district')
        for record in sorted(result.values(), key=sort_key):
            values = (record.district, record.smallest, record.total)
            print('%-13s %d %d' % values, file=f)

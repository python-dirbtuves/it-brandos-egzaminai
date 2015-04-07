#!/usr/bin/env python3

import sys
import operator
import collections


class Record(object):
    def __init__(self, district=None, smallest=sys.maxsize, total=0):
        self.district = district
        self.smallest = smallest
        self.total = total


def read_ints(lines):
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def read_row(lines):
    line = next(lines)
    city = line[:20].strip()
    district = line[20:33].strip()
    n = int(line[33:])
    return city, district, n


def main():
    with open('U2.txt') as f:
        k, = read_ints(f)
        result = collections.defaultdict(Record)
        for i in range(k):
            city, district, population = read_row(f)
            record = result[district]
            record.district = district
            record.smallest = min(record.smallest, population)
            record.total += population

    with open('U2rez.txt', 'w') as f:
        print(len(result), file=f)
        sort_key = operator.attrgetter('smallest', 'district')
        for record in sorted(result.values(), key=sort_key):
            values = (record.district, record.smallest, record.total)
            print('%-13s %d %d' % values, file=f)


if __name__ == '__main__':
    main()

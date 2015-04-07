#!/usr/bin/env python3

import collections
import operator


def read_ints(lines):
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def read_row(lines):
    line1 = next(lines)
    line2 = next(lines)
    return line1[:20].strip(), int(line1[20:]), line2[:13].strip()


def read_data(lines, k):
    """Returns aggregated data by districts and municipalities."""
    data = collections.defaultdict(lambda: collections.defaultdict(int))
    for i in range(k):
        municipality, n_schools, district = read_row(lines)
        max_n_schools = max(data[district][municipality], n_schools)
        data[district][municipality] = max_n_schools
    return data


def calculate_stats(data):
    stats = [
        (district, len(municipalities), max(municipalities.values()))
        for district, municipalities in data.items()
    ]
    stats.sort(key=operator.itemgetter(0))
    stats.sort(key=operator.itemgetter(2), reverse=True)
    return stats


def main():
    with open('U2.txt') as f:
        k, = read_ints(f)
        data = read_data(f, k)
        stats = calculate_stats(data)

    with open('U2rez.txt', 'w') as f:
        print(len(data), file=f)
        for row in stats:
            print('%-13s %d %d' % row, file=f)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import collections


def read_ints(lines):
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def read_data(lines):
    line1 = next(lines)
    line2 = next(lines)
    return line1[:20], int(line1[20:]), line2[:13]


def main():
    with open('U2.txt') as f:
        k, = read_ints(f)
        stats = collections.defaultdict(collections.defaultdict(int))
        for i in range(k):
            municipality, n_schools, region = read_data(f)
            stats[region][municipality] += n_schools

    with open('U2rez.txt', 'w') as f:
        print(len(stats), file=f)
        for region, municipalities in region.items():
            max_schools = max([max(schools) for schools in municipalities.values()])
            print('%-13s' % region, len(municipalities), max_schools, file=f)


if __name__ == '__main__':
    main()

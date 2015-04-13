#!/usr/bin/env python3


def read_ints(lines):
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def read_row(lines):
    line = next(lines)
    company = line[:10].strip()
    x, y = [int(x) for x in line[10:].split()]
    return company, x, y

def way_to_company(x, y):        # užduotyje reikalauja atskiros funkcijos
    return (abs(x) + abs(y)) * 2

def simulate_single_day(lines, n, m):
    distance = 0
    result = (0, distance, None)
    for i in range(n):
        company, x, y = read_row(lines)
        distance += way_to_company(x, y)
        if distance >= m:
            return result
        result = (i+1, distance, company)
    return result


def main():
    with open('U1.txt') as f:
        n, m = read_ints(f)
        result = simulate_single_day(f, n, m)

    with open('U1rez.txt', 'w') as f:
        print(*result, file=f)


if __name__ == '__main__':
    main()

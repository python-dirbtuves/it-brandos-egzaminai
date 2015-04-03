#!/usr/bin/env python3


def read_ints(lines):
    line = next(lines)
    return list(map(int, line.split()))


def format_results(results):
    return ' '.join(map(str, results))


def process_data(lines):
    distance = 0
    n, m = read_ints(lines)

    for i in range(n):
        distance += sum(map(abs, read_ints(lines))) * 2
        if distance > m:
            break
    clients_left = n - i - 1
    return clients_left, distance


def main():
    # Read and process input data.
    with open('U1.txt') as f:
        results = process_data(f)

    # Write results to output file.
    with open('U1rez.txt', 'w') as f:
        f.write(format_results(results))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3


def read_ints(lines):
    """Returns list of integer from next line in given iterator of lines."""
    return list(map(int, next(lines).split()))


def move(brain, step, x, y):
    """Calculate next position."""
    xd, yd = brain[step]
    return x + xd, y + yd


def walk(brain, steps, x0, y0):
    """Execute given steps and return data about how it went."""
    done = []
    x, y = x0, y0
    for step in steps:
        done.append(step)
        x, y = move(brain, step, x, y)
        if (x, y) == (x0, y0):
            return ['%-20s' % 'pasiektas tikslas'] + done + [len(done)]
    return ['%-20s' % 'sekos pabaiga'] + done + [len(done)] + [x, y]


def read_lines(brain, lines):
    x0, y0 = read_ints(lines)
    n, = read_ints(lines)
    for i in range(n):
        k, *steps = read_ints(lines)
        steps = steps[:k]
        yield walk(brain, steps[:k], x0, y0)


def main():
    brain = {
        1: (1, 1),
        2: (1, -1),
        3: (-1, -1),
        4: (-1, 1),
    }

    with open('U2rez.txt', 'w') as fout, open('U2.txt') as fin:
        for line in read_lines(brain, fin):
            print(*line, file=fout)


if __name__ == '__main__':
    main()

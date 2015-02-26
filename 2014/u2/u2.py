#!/usr/bin/env python3

class Rover(object):
    BRAIN = {
        1: (0, 1),
        2: (1, 0),
        3: (0, -1),
        4: (-1, 0),
    }

    def __init__(self, x=0, y=0):
        self.set_position(x, y)

    def set_position(self, x, y):
        self.x, self.y = x, y

    def is_in_position(self, x, y):
        return self.x == x and self.y == y

    def move(self, command):
        x, y = self.BRAIN[command]
        self.x += x
        self.y += y

    def walk_to(self, x, y, n, *commands):
        path = []
        for command in commands[:n]:
            self.move(command)
            path.append(command)
            if self.is_in_position(x, y):
                return True, path
        return False, path


def read_ints(lines):
    line = next(lines)
    return map(int, line.split())


def consume_data(lines, rover):
    r"""

    >>> data = [
    ...     '5 -1',
    ...     '8 -3',
    ...     '3',
    ...     '7 2 3 2 3 1 3 2',
    ...     '2 1 4',
    ...     '12 2 3 2 3 2 3 2 3 2 3 2 1',
    ... ]
    >>> print('\n'.join(format_results(consume_data(iter(data), Rover()))))
    pasiektas tikslas    2 3 2 3 1 3 2 7
    sekos pabaiga        1 4 2
    pasiektas tikslas    2 3 2 3 2 5

    """
    x0, y0 = read_ints(lines)
    x1, y1 = read_ints(lines)
    n, = read_ints(lines)
    for i in range(n):
        rover.set_position(x0, y0)
        yield rover.walk_to(x1, y1, *read_ints(lines))


def format_results(results):
    for found, path in results:
        message = 'pasiektas tikslas' if found else 'sekos pabaiga'
        yield '%-20s %s %s' % (message, ' '.join(map(str, path)), len(path))


def main():
    # Read and process input data.
    with open('U2.txt') as f:
        results = consume_data(f, Rover())

    # Write results to output file.
    with open('U2rez.txt', 'w') as f:
        for line in format_results(results):
            print(line, file=f)


if __name__ == '__main__':
    main()

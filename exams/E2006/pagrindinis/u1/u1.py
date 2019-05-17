from itertools import islice


def main(path):
    with (path / 'Duom1.txt').open() as f:
        R: float = 0
        k = int(next(f))
        for line in islice(f, k):
            n, *D = map(int, line.split())
            L = sum(1 / d for d in D[:n])
            R += 1 / L

    with (path / 'Rez1.txt').open('w') as f:
        f.write(str(round(R, 2)))

from os.path import join
from pathlib import Path


def add_arrays(x, y):
    return [a + b for a, b in zip(x, y)]


def access_file(file_dir: Path):
    with open(join(file_dir / "U1.txt"), 'r', encoding='utf-8') as f:
        yield from f


def main(data_file_dir: Path):
    lines = access_file(data_file_dir)
    next(lines)
    muschroom_counts: dict = {}

    for line in lines:
        day, *mushrooms = map(int, line.split())
        if sum(mushrooms) == 0:
            continue

        muschroom_counts[day] = add_arrays(muschroom_counts.get(day, [0, 0, 0]), mushrooms)

    with open(join(data_file_dir / "U1rez.txt"), 'w', encoding='utf-8') as fout:
        for day in sorted(muschroom_counts):
            mc = muschroom_counts[day]
            print(day, *mc, file=fout)
        mushroom_sum, max_day = max((sum(m), d) for d, m in muschroom_counts.items())
        print(max_day, mushroom_sum, file=fout)

from os.path import join

add_arrays = lambda x, y: [int(a) + int(b) for a, b in zip(x, y)]


def access_file(file_dir: str):
    with open(join(file_dir, "U1.txt"), 'r', encoding='utf-8') as f:
        yield from f


def main(data_file_dir: str):
    lines = access_file(data_file_dir)
    _ = next(lines)
    muschroom_counts: dict = {}
    days = []

    for line in lines:
        if " 0 0 0" in line:
            continue

        days.append(int(line[:2]))
        muschroom_counts[days[-1]] = add_arrays(muschroom_counts.get(days[-1], [0, 0, 0]), line.split()[1:])

    d, m = 0, 0
    with open(join(data_file_dir, "U1rez.txt"), 'w', encoding='utf-8') as fout:
        for day in sorted(list(set(days))):
            mc = muschroom_counts[day]
            print("{} {} {} {}".format(day, *mc), file=fout)
            d, m = (d, m) if m >= sum(mc) else (day, sum(mc))
        print(d, m, file=fout)

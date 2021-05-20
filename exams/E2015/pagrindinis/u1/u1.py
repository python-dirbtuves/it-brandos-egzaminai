from pathlib import Path


def read_data(path: Path):
    data = (path / 'U1.txt').read_text()
    return list(map(int, data.split()))


def simulate(data):
    cups = list(map(lambda x: 10, range(0, 10)))
    eat_log = list(map(lambda x: 0, range(0, 20)))

    # Initial greedy and unfriendly eating of girlz
    for i in range(0, 10):
        eat_log[i] += data[i]
        cups[i] -= data[i]

    # Eat and pass, each girl
    for i, cup in enumerate(cups):
        for j in range(cup):
            eat_log[i + j + 1] += 1

    return eat_log


def write_data(path, data):
    (path / 'U1rez.txt').write_text(' '.join(map(str, data)))


def main(path):
    data = read_data(path)
    result = simulate(data)
    write_data(path, result)

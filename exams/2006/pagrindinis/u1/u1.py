def main(path):
    with (path / 'Duom1.txt').open() as f:
        lines = f.readlines()
        k, *lines = lines
        k = int(k)
        R = 0
        for line in lines[:k]:
            n, *D = map(int, line.split())
            L = sum(1/d for d in D[:n])
            R += 1/L
    with (path / 'Rez1.txt').open('w') as f:
        f.write(str(round(R, 2)))

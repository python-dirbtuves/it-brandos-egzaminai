def main(path):
    with open(path / 'U1.txt') as f:
        height, width = map(int, next(f).split())
        answer = '\n'.join([
            ';'.join([
                ''.join(f'{x:02X}' for x in map(int, next(f).split()))
                for i in range(width)
            ])
            for j in range(height)
        ])

    with open(path / 'U1rez.txt', 'w') as f:
        f.write(answer)

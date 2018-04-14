import u1


def test(path):
    (path / 'U1.txt').write(
        '8',
        '2 1 3',
        '1 2 3',
        '3 3 2',
        '2 1 3',
        '2 3 2',
        '3 3 2',
        '2 2 2',
        '1 3 3',
        '2',
    )
    u1.main(path)
    (path / 'U1rez.txt').read() == [
        '2 4 2',
        '2',
    ]

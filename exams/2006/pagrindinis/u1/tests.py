import u1


def test(path):
    (path / 'Duom1.txt').write(
        '3',
        '2 15 41',
        '4 1 2 3 4',
        '3 22 11 24',
    )
    u1.main(path)
    assert (path / 'Rez1.txt').read() == [
        '17.08',
    ]

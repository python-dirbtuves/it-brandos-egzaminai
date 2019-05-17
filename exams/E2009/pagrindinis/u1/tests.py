from exams.E2009.pagrindinis.u1 import u1


def test(path):
    (path / 'U1.txt').write(
        '6',
        '10 7 6 4 3 1',
        '10 0 8 4 3 0',
        '4',
        '8 6 4 1',
        '1 1 50 0',
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '8 21',
        '6 0',
        '4 1',
        '1 1',
        '23',
        '10 21',
        '7 0',
        '6 0',
        '4 1',
        '3 0',
        '1 0',
        '22',
    ]

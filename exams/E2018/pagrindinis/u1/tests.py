from exams.E2018.pagrindinis.u1 import u1


def test(path):
    (path / 'U1.txt').write(
        '5',
        'Z 14',
        'R 12',
        'G 20',
        'R 5',
        'R 6',
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '7',
        'G = 6',
        'Z = 0',
        'R = 9',
    ]

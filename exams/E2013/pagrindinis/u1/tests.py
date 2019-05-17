from exams.E2013.pagrindinis.u1 import u1


def test(path):
    (path / 'U1.txt').write(
        '5 30',
        'Siuntuva  2 3',
        'Auda      3 -1',
        'Kostisa   -3 -2',
        'Linga     3 0',
        'Austuva   -2 -4',
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '3 28 Kostisa',
    ]

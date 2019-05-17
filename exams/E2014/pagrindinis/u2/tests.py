from exams.E2014.pagrindinis.u2 import u2


def test(path):
    (path / 'U2.txt').write(
        '5 -1',
        '8 -3',
        '3',
        '7 2 3 2 3 1 3 2',
        '2 1 4',
        '12 2 3 2 3 2 3 2 3 2 3 2 1',
    )
    u2.main(path)
    assert (path / 'U2rez.txt').read() == [
        'pasiektas tikslas    2 3 2 3 1 3 2 7',
        'sekos pabaiga        1 4 2',
        'pasiektas tikslas    2 3 2 3 2 5',
    ]

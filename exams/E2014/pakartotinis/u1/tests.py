from exams.E2014.pakartotinis.u1 import u1


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
    assert (path / 'U1rez.txt').read() == [
        '2 4 2',
        '2',
    ]


def test_director_vote(path):
    (path / 'U1.txt').write(
        '2',
        '1 2 3',
        '1 2 3',
        '2',
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '2 0 0',
        '1',
    ]

from exams.E2014.bandomasis.u1 import u1


def test(path):
    (path / 'U1.txt').write(
        '5 30',
        '2 3',
        '3 -1',
        '-2 -4',
        '-3 0',
        '-2 4',
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '1 36',
    ]

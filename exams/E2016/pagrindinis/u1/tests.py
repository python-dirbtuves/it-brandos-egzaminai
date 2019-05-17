from exams.E2016.pagrindinis.u1 import u1


def test_a_pvz(path):
    (path / 'U1.txt').write(
        '6',
        '5000',
        '4500',
        '5500',
        '3500',
        '10000',
        '5650',
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '10000 3',
    ]


def test_b_pvz(path):
    (path / 'U1.txt').write(
        '3',
        '3000',
        '3500',
        '2000',
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '3500 0',
    ]

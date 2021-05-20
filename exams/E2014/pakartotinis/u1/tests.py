from exams.E2014.pakartotinis.u1 import u1
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U1.txt', [
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
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '2 4 2',
        '2',
    ]


def test_director_vote(path):
    write(path / 'U1.txt', [
        '2',
        '1 2 3',
        '1 2 3',
        '2',
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '2 0 0',
        '1',
    ]

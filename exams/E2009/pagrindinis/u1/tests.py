from exams.E2009.pagrindinis.u1 import u1
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U1.txt', [
        '6',
        '10 7 6 4 3 1',
        '10 0 8 4 3 0',
        '4',
        '8 6 4 1',
        '1 1 50 0',
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
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

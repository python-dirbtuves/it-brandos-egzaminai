from exams.E2014.bandomasis.u1 import u1
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U1.txt', [
        '5 30',
        '2 3',
        '3 -1',
        '-2 -4',
        '-3 0',
        '-2 4',
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '1 36',
    ]

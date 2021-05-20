from exams.E2018.pagrindinis.u1 import u1
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U1.txt', [
        '5',
        'Z 14',
        'R 12',
        'G 20',
        'R 5',
        'R 6',
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '7',
        'G = 6',
        'Z = 0',
        'R = 9',
    ]

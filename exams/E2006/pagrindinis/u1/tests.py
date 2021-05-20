from exams.E2006.pagrindinis.u1 import u1
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'Duom1.txt', [
        '3',
        '2 15 41',
        '4 1 2 3 4',
        '3 22 11 24',
    ])
    u1.main(path)
    assert read(path / 'Rez1.txt') == [
        '17.08',
    ]

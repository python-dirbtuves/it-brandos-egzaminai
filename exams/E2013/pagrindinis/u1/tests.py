from exams.E2013.pagrindinis.u1 import u1
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U1.txt', [
        '5 30',
        'Siuntuva  2 3',
        'Auda      3 -1',
        'Kostisa   -3 -2',
        'Linga     3 0',
        'Austuva   -2 -4',
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '3 28 Kostisa',
    ]

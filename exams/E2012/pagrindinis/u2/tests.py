from exams.E2012.pagrindinis.u2 import u2
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U2.txt', [
        '2 3',
        'Hermis    6 1 2',
        'Hera      2 6 6',
    ])
    u2.main(path)
    assert read(path / 'U2rez.txt') == [
        'Hera      14',
    ]

from exams.E2017.pagrindinis.u1 import u1
from exams.testing import read
from exams.testing import write


def test_a_pvz(path):
    write(path / 'U1.txt', [
        '2 3',
        '0 128 0',
        '255 0 0',
        '255 255 255',
        '255 255 0',
        '255 0 0',
        '255 255 0'
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '008000;FF0000;FFFFFF',
        'FFFF00;FF0000;FFFF00'
    ]

from exams.E2016.pagrindinis.u1 import u1
from exams.testing import read
from exams.testing import write


def test_a_pvz(path):
    write(path / 'U1.txt', [
        '6',
        '5000',
        '4500',
        '5500',
        '3500',
        '10000',
        '5650',
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '10000 3',
    ]


def test_b_pvz(path):
    write(path / 'U1.txt', [
        '3',
        '3000',
        '3500',
        '2000',
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '3500 0',
    ]

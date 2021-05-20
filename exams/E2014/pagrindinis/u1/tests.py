from exams.E2014.pagrindinis.u1 import u1
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U1.txt', [
        '6',
        '15 10 22',
        '15 40 13',
        '23 26 26',
        '110 30 58',
        '33 33 32',
        '0 56 0',
        '2 1 3',
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '196 195 151',
        '6 12 6',
        '2',
    ]


def test_without_units():
    results = u1.count_votes(iter(['0', '1 3 2']))
    assert results == ([0, 0, 0], [1, 3, 2], 2)

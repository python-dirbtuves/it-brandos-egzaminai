from exams.E2007.pagrindinis.u1 import u1
from exams.E2007.pagrindinis.u1 import u1_simple
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U1.txt', [
        "11",
        "2 8 4 0",
        "3 1 0 9",
        "1 2 3 4",
        "5 4 14 2",
        "2 4 4 4",
        "3 0 0 0",
        "15 25 45 13",
        "28 13 13 13",
        "16 2 0 2",
        "16 5 15 25",
        "3 4 44 444",
    ])
    u1.main(path)
    assert read(path / 'U1rez.txt') == [
        '1 2 3 4',
        '2 12 8 4',
        '3 5 44 453',
        '5 4 14 2',
        '15 25 45 13',
        '16 7 15 27',
        '28 13 13 13',
        '3 502',
    ]
    u1_simple.main(path)
    assert read(path / 'U1rez.txt') == [
        '1 2 3 4',
        '2 12 8 4',
        '3 5 44 453',
        '5 4 14 2',
        '15 25 45 13',
        '16 7 15 27',
        '28 13 13 13',
        '3 502',
    ]

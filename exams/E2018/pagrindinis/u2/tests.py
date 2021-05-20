from exams.E2018.pagrindinis.u2 import u2
from exams.testing import Path
from exams.testing import read
from exams.testing import write


def test(path: Path):
    write(path / 'U2.txt', [
        '6',
        'Petras A. Petraitis 15 20 00',
        'Jurgis Jurgutis     16 12 12',
        'Rimas Jonas         15 15 59',
        'Zigmas Nosis        16 23 9',
        'Romas Senasis       15 15 15',
        'Rytis Uosis Ainis   16 23 9',
        '5',
        'Zigmas Nosis        16 43 15',
        'Petras A. Petraitis 15 50 10',
        'Romas Senasis       16 5 35',
        'Rytis Uosis Ainis   16 55 59',
        'Jurgis Jurgutis     16 42 22',
    ])
    u2.main(path)
    assert read(path / 'U2rez.txt') == [
        'Zigmas Nosis        20 6',
        'Jurgis Jurgutis     30 10',
        'Petras A. Petraitis 30 10',
        'Rytis Uosis Ainis   32 50',
        'Romas Senasis       50 20',
    ]

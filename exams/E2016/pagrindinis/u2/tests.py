from exams.E2016.pagrindinis.u2 import u2
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U2.txt', [
        '10',
        'prisitraukimai       10',
        'atsispaudimai        15',
        'atsilenkimai         12',
        'prisitraukimai       4',
        'atsilenkimai         15',
        'atsilenkimai         10',
        'prisitraukimai       12',
        'atsilenkimai         10',
        'atsispaudimai        2',
        'atsispaudimai        2',
    ])
    u2.main(path)
    assert read(path / 'U2rez.txt') == [
        'atsilenkimai         47',
        'prisitraukimai       26',
        'atsispaudimai        19',
    ]

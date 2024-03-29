from exams.E2006.pagrindinis.u2 import u2
from exams.E2006.pagrindinis.u2 import u2_simple
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'Duom2.txt', [
        '6 70 10 15',
        'Elektrėnai     50.5',
        'Žiežmariai     20',
        'Kaunas         22.35',
        'Raseiniai      80',
        'Kryžkalnis     20',
        'Klaipėda       100.8',
    ])
    u2.main(path)
    assert read(path / 'Rez2.txt') == [
        'Elektrėnai     10 val. 58 min.',
        'Žiežmariai     11 val. 15 min.',
        'Kaunas         11 val. 34 min.',
        'Raseiniai      12 val. 43 min.',
        'Kryžkalnis     13 val. 0 min.',
        'Klaipėda       14 val. 26 min.',
    ]
    u2_simple.main(path)
    assert read(path / 'Rez2.txt') == [
        'Elektrėnai     10 val. 58 min.',
        'Žiežmariai     11 val. 15 min.',
        'Kaunas         11 val. 34 min.',
        'Raseiniai      12 val. 43 min.',
        'Kryžkalnis     13 val. 0 min.',
        'Klaipėda       14 val. 26 min.',
    ]

import u2


def test(path):
    (path / 'Duom1.txt').write(
        '6 70 10 15',
        'Elektrėnai      50.5',
        'Žiežmariai      20',
        'Kaunas          22.35',
        'Raseiniai       80',
        'Kryžkalnis      20',
        'Klaipėda        100.8',
    )
    u2.main(path)
    assert (path / 'Rez1.txt').read() == [
        'Elektrėnai      10 val. 58 min.',
        'Žiežmariai      11 val. 15 min.',
        'Kaunas          11 val. 34 min.',
        'Raseiniai       12 val. 43 min.',
        'Kryžkalnis      13 val. 0 min.',
        'Klaipėda        14 val. 26 min.',
    ]

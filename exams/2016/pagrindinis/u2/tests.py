import u2


def test(path):
    (path / 'U2.txt').write(
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
    )
    u2.main(path)
    assert (path / 'U2rez.txt').read() == [
        'atsilenkimai         47',
        'prisitraukimai       26',
        'atsispaudimai        19',
    ]

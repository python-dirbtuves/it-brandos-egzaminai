import os


def test():
    import u2

    u2.main()

    with open('U2rez.txt') as f:
        assert f.read() == '\n'.join([
            'atsilenkimai         47',
            'prisitraukimai       26',
            'atsispaudimai        19',
            '',
        ])

    os.unlink('U2rez.txt')

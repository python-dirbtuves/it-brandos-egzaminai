from exams.E2012.pagrindinis.u2 import u2


def test(path):
    (path / 'U2.txt').write(
        '2 3',
        'Hermis    6 1 2',
        'Hera      2 6 6',
    )
    u2.main(path)
    assert (path / 'U2rez.txt').read() == [
        'Hera      14',
    ]

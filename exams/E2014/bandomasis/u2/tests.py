import pathlib

from exams.E2014.bandomasis.u2 import u2


def test(tmpdir):
    tmpdir.join('U2.txt').write('\n'.join([
        '5',
        'Jieznas             1',
        'Kauno',
        'Jonava              4',
        'Kauno',
        'Kavarskas           3',
        'Utenos',
        'Lazdijai            1',
        'Alytaus',
        'Simnas              1',
        'Alytaus',
    ]))
    u2.main(pathlib.Path(tmpdir))
    assert tmpdir.join('U2rez.txt').read().splitlines() == [
        '3',
        'Kauno         2 4',
        'Utenos        1 3',
        'Alytaus       2 1',
    ]

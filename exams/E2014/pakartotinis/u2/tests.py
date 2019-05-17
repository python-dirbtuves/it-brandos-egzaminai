import pathlib

from exams.E2014.pakartotinis.u2 import u2


def test(tmpdir):
    tmpdir.join('U2.txt').write('\n'.join([
        '1 1',
        '3',
        '9 1 4 1 2 3 2 3 4 1',
        '1 1',
        '3 2 3 2',
    ]))
    u2.main(pathlib.Path(tmpdir))
    assert tmpdir.join('U2rez.txt').read().splitlines() == [
        'pasiektas tikslas    1 4 1 2 3 2 3 4 8',
        'sekos pabaiga        1 1 2 2',
        'sekos pabaiga        2 3 2 3 2 -2',
    ]

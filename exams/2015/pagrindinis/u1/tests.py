import pytest
import u1


@pytest.mark.parametrize('i,o', [
    ('6 3 2 8 0 5 4 9 1 3', '6 4 4 11 4 9 8 14 7 8 6 4 4 3 3 2 2 1 0 0'),
    ('0 0 0 0 0 0 0 0 0 0', '0 1 2 3 4 5 6 7 8 9 10 9 8 7 6 5 4 3 2 1'),
    ('10 9 8 7 6 5 4 3 2 1', '10 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1 0'),
    ('5 4 3 2 1 0 0 0 0 0', '5 5 5 5 5 5 5 6 6 7 7 7 6 6 5 5 4 3 2 1')
])
def test(path, i, o):
    (path/'U1.txt').write(i)
    u1.main(path)
    assert (path/'U1rez.txt').read() == [o]

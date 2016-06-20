import os
import u1


def test():
    u1.main()

    with open('U1rez.txt') as f:
        lines = f.read().splitlines()

    assert lines == ['10000 3']

    os.unlink('U1rez.txt')


def test_no_matches(mocker):
    mocker.patch('u1.weights', return_value=[3000, 3500, 2000])

    u1.main()

    with open('U1rez.txt') as f:
        lines = f.read().splitlines()

    assert lines == ['3500 0']

    os.unlink('U1rez.txt')

import os
import u1


def test():
    u1.main()

    with open('U1rez.txt') as f:
        lines = f.read().splitlines()

    assert lines == [
        '196 195 151',
        '6 12 6',
        '2',
    ]

    os.unlink('U1rez.txt')


def test_without_units():
    results = u1.count_votes(iter(['0', '1 3 2']))
    assert results == ([0, 0, 0], [1, 3, 2], 2)

import os
import unittest

import u1


class U2Tests(unittest.TestCase):
    def test(self):
        u1.main()

        with open('U1rez.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, [
            '196 195 151',
            '6 12 6',
            '2',
        ])

        os.unlink('U1rez.txt')

    def test_without_units(self):
        results = u1.count_votes(iter(['0', '1 3 2']))
        self.assertEqual(results, ([0, 0, 0], [1, 3, 2], 2))

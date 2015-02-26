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

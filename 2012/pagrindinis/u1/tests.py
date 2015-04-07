import os
import unittest

import u1


class U1Tests(unittest.TestCase):
    def test(self):
        u1.main()

        with open('U1rez.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, [
            '9 13 14 25 33',
            '33 32',
            '5 40',
        ])

        os.unlink('U1rez.txt')

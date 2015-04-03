import os
import unittest

import u1


class U1Tests(unittest.TestCase):
    def test(self):
        u1.main()

        with open('U1rez.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, [
            '2 4 2',
            '2',
        ])

        os.unlink('U1rez.txt')

import os
import unittest

import u2


class U2Tests(unittest.TestCase):
    def test(self):
        u2.main()

        with open('U2rez.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, [
            'Hera      14',
        ])

        os.unlink('U2rez.txt')

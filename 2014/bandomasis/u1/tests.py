import os
import unittest

import u1


class U1Tests(unittest.TestCase):
    def test(self):
        u1.main()

        with open('U1rez.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, ['1 36'])

        os.unlink('U1rez.txt')

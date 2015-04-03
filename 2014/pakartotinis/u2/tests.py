import os
import unittest

import u2


class U2Tests(unittest.TestCase):
    def test(self):
        u2.main()

        with open('U2rez.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, [
            'pasiektas tikslas    1 4 1 2 3 2 3 4 8',
            'sekos pabaiga        1 1 2 2',
            'sekos pabaiga        2 3 2 3 2 -2',
        ])

        os.unlink('U2rez.txt')

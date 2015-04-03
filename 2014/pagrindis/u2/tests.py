import os
import unittest

import u2


class U2Tests(unittest.TestCase):
    def test(self):
        u2.main()

        with open('U2rez.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, [
            'pasiektas tikslas    2 3 2 3 1 3 2 7',
            'sekos pabaiga        1 4 2',
            'pasiektas tikslas    2 3 2 3 2 5',
        ])

        os.unlink('U2rez.txt')

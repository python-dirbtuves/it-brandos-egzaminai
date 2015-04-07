import os
import unittest

import u2


class U2Tests(unittest.TestCase):
    def test(self):
        u2.main()

        with open('U2rez.txt') as f:
            lines = f.read().splitlines()

        self.assertEqual(lines, [
            '3',
            'Kauno         2 4',
            'Utenos        1 3',
            'Alytaus       2 1',
        ])

        os.unlink('U2rez.txt')

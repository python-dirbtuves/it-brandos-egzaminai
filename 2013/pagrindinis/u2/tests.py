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
            'Utenos        753 80796',
            'Alytaus       1673 95389',
            'Vilniaus      5246 563860',
        ])

        os.unlink('U2rez.txt')

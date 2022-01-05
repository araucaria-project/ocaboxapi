import os.path
import unittest

from ocaboxapi import Observatory
from ocaboxapi.config import Config
from ocaboxapi.coo import check_equatorial_coordinates, check_horizontal_coordinates


class CoordinatesTestCase(unittest.TestCase):
    def test_equatorial(self):
        to_check = [
            (33.12, 33.12, -21.05, -21.05),
            ('12:30:00.0', 12.5/24*360, '-33:12:40.23', -(33+(12+40.23/60)/60)),
        ]
        for ra, cra, dec, cdec in to_check:
            nra, ndec = check_equatorial_coordinates(ra, dec)
            self.assertAlmostEqual(nra, cra)
            self.assertAlmostEqual(ndec, cdec)

    def test_horizontal(self):
        to_check = [
            (33.12, 33.12, -21.05, -21.05),
            ('12:30:00.0', 12.5, '-33:12:40.23', -(33+(12+40.23/60)/60)),
        ]
        for az, caz, alt, calt in to_check:
            naz, nalt = check_horizontal_coordinates(az, alt)
            self.assertAlmostEqual(naz, caz)
            self.assertAlmostEqual(nalt, calt)



if __name__ == '__main__':
    unittest.main()

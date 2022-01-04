import unittest

from ocaboxapi import Observatory


class ObservatoryTestCase(unittest.TestCase):
    def test_instancing_device(self):
        ob = Observatory()
        self.assertIsInstance(ob, Observatory)

    def test_connecting_device(self):
        ob = Observatory()
        ob.connect('default')


if __name__ == '__main__':
    unittest.main()

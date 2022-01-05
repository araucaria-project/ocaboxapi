import os.path
import unittest

from ocaboxapi import Observatory
from ocaboxapi.config import Config


class ObservatoryTestCase(unittest.TestCase):
    def test_instancing_device(self):
        ob = Observatory()
        self.assertIsInstance(ob, Observatory)

    def test_connecting_device(self):
        ob = Observatory()
        ob.connect('default')

    def test_tree_structure(self):
        cfg = Config.instance_from_files([os.path.join(os.path.dirname(__file__), 'test.cfg.yaml')])
        ob = Observatory(configuration=cfg)
        ob.connect()
        c = ob.component_by_absolute_sys_id('obs.t1.focuser')
        self.assertEqual(c.root, ob)


if __name__ == '__main__':
    unittest.main()

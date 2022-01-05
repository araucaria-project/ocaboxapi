import os
import unittest

from ocaboxapi.config import Config


class ConfigTestCase(unittest.TestCase):

    def test_singleton_instance(self):
        c1 = Config.global_instance()
        c2 = Config.global_instance()
        self.assertEqual(c1, c2)

    def test_default(self):
        cfg = Config.instance_from_files([os.path.join(os.path.dirname(__file__), 'test.cfg.yaml')])
        x = cfg.data['default']['observatory']['components']['t1']['kind']
        self.assertEqual(x, 'telescope')


if __name__ == '__main__':
    unittest.main()

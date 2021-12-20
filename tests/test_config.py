import unittest

from ocaboxapi.config import Config


class ConfigTestCase(unittest.TestCase):

    def test_singleton_instance(self):
        c1 = Config.global_instance()
        c2 = Config.global_instance()
        self.assertEqual(c1, c2)

    def test_default(self):
        x = Config.global_config()['default']['observatory']['components']['ls']['kind']
        self.assertEqual(x, 'telescope')


if __name__ == '__main__':
    unittest.main()

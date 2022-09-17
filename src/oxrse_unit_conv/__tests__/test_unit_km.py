import unittest
from ..units import km, m


class TestKilometer(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(km.si_unit.matches(m))

    def test_basic_conversion(self):
        self.assertEqual(km.to_si(1), 1_000)
        self.assertEqual(km.to_unit(10, km), 10)


if __name__ == '__main__':
    unittest.main()

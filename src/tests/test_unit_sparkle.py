import unittest
from oxrse_unit_conv.units import sparkle, candela


class TestSparkle(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(sparkle.si_unit.matches(candela))

    def test_to_si(self):
        self.assertEqual(sparkle.to_si(1), 5)
    
    def test_from_si(self):
        self.assertEqual(candela.to_unit(5, sparkle), 1)


if __name__ == '__main__':
    unittest.main()

import unittest
from oxrse_unit_conv.units import milimeter, m


class TestMilimeter(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(milimeter.si_unit.matches(m))

    def test_basic_conversion(self):
        self.assertEqual(milimeter.to_si(100), 0.1)
        self.assertEqual(milimeter.to_unit(10, m), 0.01, 8)


if __name__ == '__main__':
    unittest.main()

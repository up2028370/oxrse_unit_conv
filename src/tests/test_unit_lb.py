import unittest
from oxrse_unit_conv.units import lb, kg


class TestPound(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(lb.si_unit.matches(kg))

    def test_basic_conversion(self):
        self.assertEqual(lb.to_si(1), 0.4535924)
        self.assertAlmostEqual(lb.to_unit(10, lb), 10, 8)


if __name__ == '__main__':
    unittest.main()

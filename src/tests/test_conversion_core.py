import unittest
from oxrse_unit_conv.meta import classes
from oxrse_unit_conv.units import kilometer, m, m2, m3, s, hour


class TestConversionCore(unittest.TestCase):
    def test_matches(self):
        self.assertTrue(m.matches(m))

    def test_basic_conversion(self):
        self.assertEqual(kilometer.to_si(1), 1_000)
        self.assertEqual(kilometer.to_unit(10, kilometer), 10)

    def test_converting_from_si(self):
        self.assertEqual(m.to_unit(1_000, kilometer), 1)

    def test_exponented_conversion(self):
        km2 = classes.Unit(
            name='square kilometer',
            abbr='km2',
            si=m2,
            to_si_fun=lambda x: x * 1000,
            exponent=2
        )
        self.assertEqual(km2.to_si(1), 1_000_000)
        self.assertEqual(km2.to_unit(10, km2), 10)

    def test_nonstandard_inversion(self):
        hertz = classes.Unit(
            name='hertz',
            abbr='Hz',
            si=s,
            to_si_fun=lambda x: 1 / x,
            from_si_fun=lambda x: 1 / x
        )
        self.assertEqual(hertz.to_si(1000), 0.001)
        self.assertEqual(hertz.to_unit(10, hertz), 10)

    def test_unit_to_unit_conversion(self):
        foot = classes.Unit('foot', 'ft', m, lambda x: x * 0.3048)
        furlong = classes.Unit('furlong', 'furlong', m, lambda x: x * 201.168)
        self.assertEqual(foot.to_unit(660, furlong), 1)
        self.assertEqual(furlong.to_unit(1, foot), 660)

    def test_exponented_unit_to_unit_conversion(self):
        foot3 = classes.Unit('cubic foot', 'ft2', m3, lambda x: x * 0.3048, exponent=3)
        furlong3 = classes.Unit('cubic furlong', 'furlong', m3, lambda x: x * 201.168, exponent=3)
        self.assertAlmostEqual(foot3.to_unit(287_496_000, furlong3), 1, 8)  # floating point errors
        self.assertAlmostEqual(furlong3.to_unit(1, foot3), 287_496_000, 8)  # floating point errors

    def test_dimensionality_constraint(self):
        try:
            exception = False
            hour.to_unit(10, kilometer)
        except BaseException as e:
            # workaround for the standard approach not matching e to classes.DimensionError
            self.assertEqual(type(e).__name__, classes.DimensionError.__name__)
            exception = True
        self.assertTrue(exception)
        try:
            exception = False
            kilometer.to_unit(10, hour)
        except BaseException as e:
            # workaround for the standard approach not matching e to classes.DimensionError
            self.assertEqual(type(e).__name__, classes.DimensionError.__name__)
            exception = True

    def test_exponent_constraint(self):
        foot = classes.Unit('foot', 'ft', m, lambda x: x * 0.3048)
        foot3 = classes.Unit('cubic foot', 'ft2', m3, lambda x: x * 0.3048, exponent=3)
        with self.assertRaises(classes.ExponentError):
            foot3.to_unit(10, foot)
        with self.assertRaises(classes.ExponentError):
            foot.to_unit(10, foot3)

    def test_offset_exponents(self):
        hectare = classes.Unit('hectare', 'ha', m2, lambda x: x * 10_000)
        acre = classes.Unit('acre', 'a', m2, lambda x: x * 4_046.8564)
        km2 = classes.Unit('square kilometer', 'km2', m2, lambda x: x * 1000, exponent=2)
        self.assertEqual(hectare.to_unit(1, km2), 0.01)
        self.assertEqual(km2.to_unit(1, hectare), 100)
        self.assertAlmostEqual(acre.to_unit(1, km2), 0.00404686, 8)
        self.assertAlmostEqual(km2.to_unit(1, acre), 247.105, 3)
        self.assertAlmostEqual(hectare.to_unit(2, acre), 4.94211, 5)
        self.assertAlmostEqual(acre.to_unit(5, hectare), 2.02343, 5)


if __name__ == '__main__':
    unittest.main()

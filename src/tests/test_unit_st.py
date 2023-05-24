import unittest
from oxrse_unit_conv.units import kg, st

class TestStone(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(st.si_unit.matches(kg))
    
    def test_conversion(self):
        self.assertEqual(st.to_si(1), 0.157473)
        self.assertAlmostEquals(st.to_unit(10, st),10, 6)

if __name__ == '_main_':
    unittest.main()
        



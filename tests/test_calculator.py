import unittest
from calculations.calculator import Calculator


class TestCalculator(unittest.TestCase):

    calc = Calculator()

    def test_to_fixed(self):
        result = self.calc.to_fixed(4.1235, 2)
        self.assertTrue(result, 4.12)

    def test_to_fixed_negative(self):
        result = self.calc.to_fixed(-4.1235, 2)
        self.assertTrue(result, -4.12)

    # def test_calculate_analytical(self):
    #     self.calc.data_entry(1, 12, 5)
    #     self.calc.calculate_analytical()
    #     self.assertTrue(self.calc.indicator.indicators["Analytical"]["Math expectation"], 6)
    #     self.assertTrue(self.calc.indicator.indicators["Analytical"]["Dispersion"], 6)
    #     self.assertTrue(self.calc.indicator.indicators["Analytical"]["Standard Deviation"], 6)
    #     self.assertTrue(self.calc.indicator.indicators["Analytical"]["Variation coefficient"], 6)
    #     self.assertTrue(self.calc.indicator.indicators["Analytical"]["X gamma"], 6)





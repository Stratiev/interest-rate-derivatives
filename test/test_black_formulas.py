import unittest
from analytic_formulas import Swaption


class TestSwaption(unittest.TestCase):

    strike = 0.02
    swap_rate = 0.03
    volatility = 0.2
    expiry = 1
    annuity = 10

    def test_price(self):
        swaption = Swaption(self.annuity, self.swap_rate, self.strike, self.volatility, self.expiry)
        self.assertEqual(swaption.price(), 0.10038495064659411)


if __name__ == '__main__':
    unittest.main()


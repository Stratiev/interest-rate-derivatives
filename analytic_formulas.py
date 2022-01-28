from interest_rates import RateCurve
import numpy as np
from scipy.stats import norm


class Swaption:
    """
    A swaption is an option to enter into a swap agreement.

    :param annuity: The annuity of the swap. We don't need the start date, payment intervals
        and maturity of the swap as long as we have the annuity.
    :param strike: The strike is the interest rate of the underlying swap.
    :param swap_rate: The swap rate is the current market swap rates for the corresponding start and maturity.
    :param volatility: This is the volatility of the swap rates.
    :param expiry: This is the expiry of the swaption and also the start of the underlying swap.
    """

    def __init__(self, annuity, swap_rate, strike, volatility, expiry):
        self.annuity = annuity
        self.swap_rate = swap_rate
        self.strike = strike
        self.volatility = volatility
        self.expiry = expiry
        self.d1 = (np.log(swap_rate / strike) + volatility**2 * expiry/2) / (volatility * np.sqrt(expiry))
        self.d2 = (np.log(swap_rate / strike) - volatility**2 * expiry/2) / (volatility * np.sqrt(expiry))

    def price(self):
        """
        This formula assumes that the market swap rates are log-normally distributed.
        """
        black_formula = self.annuity * (self.swap_rate * norm.cdf(self.d1) - self.strike * norm.cdf(self.d2))
        return black_formula

    def payoff(self):
        # TODO
        # This is misleading. Here self.swap_rate should be the swap rate at expiry, whereas above
        # it is the market swap rate at the creation of the swaption contract.
        """This should be used when pricing using Monte Carlo."""
        return self.annuity * (self.swap_rate - self.strike)






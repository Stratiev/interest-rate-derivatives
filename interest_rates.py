import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class RateCurve:

    def __init__(self):
        self.load_yield_data()
        self.compute_discount_data()

    def load_yield_data(self):
        # TODO
        # Add some other default yield.
        # Add the functionality to take yield data from an MC simulation.
        self.yield_data = [ y / 100 for y in pd.read_csv("USTREASURY-YIELD.csv").iloc[0].to_list()[1:] ]
        self.basic_maturities = [1/12, 1/6, 1/4, 1/2, 1, 2, 3, 5, 7, 10, 20, 30]

    def compute_discount_data(self):
        self.discount_data = [np.exp( - t * y) for t, y in zip(self.basic_maturities, self.yield_data)]

    def get_yield_curve(self, maturities):
        """Interpolates the yield curve to the required maturities."""
        # TODO
        # Make this into a proper bootstrap, not a linear interpolation.
        yield_curve = np.interp(maturities, self.basic_maturities, self.yield_data)
        return {t:d for t, d in zip(maturities, yield_curve) }

    def get_discount_curve(self, maturities):
        """Interpolates the discount curve to the required maturities."""
        # TODO
        # Make this into a proper bootstrap, not a linear interpolation.
        discount_curve = np.interp(maturities, self.basic_maturities, self.discount_data).tolist()
        return {t:d for t, d in zip(maturities, discount_curve) }




class Swap:

    def __init__(self, maturity, swap_start=0):
        if not isinstance(maturity, int):
            raise ValueError("Currently only int maturities supported.")
        self.T = maturity
        self.swap_start = swap_start
        # How often the swap payments are settled.
        self.settlement_frequency = 0.5
        self.settlement_number = int(self.T / self.settlement_frequency)
        self.settlement_times = [self.settlement_frequency * i for i in range(self.swap_start, self.settlement_number + 1)]
        self.discount_curve = RateCurve().get_discount_curve(self.settlement_times)

    def swap_rate(self):
        # Return the swap rate for the specified maturity for a spot-starting swap.
        return (self.discount_curve[self.swap_start] - self.discount_curve[self.T]) / self.annuity()

    def annuity(self):
        # Return the annuity for the specified maturity.
        annuity = sum([self.settlement_frequency * self.discount_curve[t] for t in self.settlement_times])
        return annuity
        


co_initial_swap_rates = [Swap(i).swap_rate() for i in range(30)]
co_terminal_swap_rates = [Swap(30, swap_start=i).swap_rate() for i in range(29)]
plt.plot(co_initial_swap_rates)
plt.plot(co_terminal_swap_rates)
plt.show()



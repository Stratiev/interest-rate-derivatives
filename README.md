# Interest Rate Derivatives
Trying to implement what I've learned so far in the world of interest rate derivatives.

For now my plan is to implement the following functionality:

- Price swaps from bond yields and vice-versa.
  - This is done in `interest_rates.py`.
- Implement basic Black formulas for swaptions, caplets and floorlets.
  - This is done in `analytic_formulas.py`.
- Price forwards.
- Run a Monte Carlo on forwards for a small set of maturities.
  - [Heath-Jarrow-Morton (HJM) model](https://en.wikipedia.org/wiki/Heath%E2%80%93Jarrow%E2%80%93Morton_framework)
  - [Brace-Gatarek-Musiela (BGM) model](https://en.wikipedia.org/wiki/LIBOR_market_model)
  - [Ho-Lee model](https://en.wikipedia.org/wiki/Ho%E2%80%93Lee_model)
  - [Vašíček model](https://en.wikipedia.org/wiki/Vasicek_model#:~:text=In%20finance%2C%20the%20Vasicek%20model,one%20source%20of%20market%20risk.)
  - [Cox-Ingersoll-Ross model](https://en.wikipedia.org/wiki/Cox%E2%80%93Ingersoll%E2%80%93Ross_model)
- Bootstrap yield curve.
- Price swaptions.
- Price caplets.
- Price floorets.

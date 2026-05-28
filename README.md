# Nvidia Stock Price Simulator

A Monte Carlo stock price simulator built using Geometric Brownian Motion (GBM). The model pulls real market data via yfinance and simulates 100 possible trajectories for Nvidia's stock price over one trading year, using two years of historical data to derive model parameters.

## The Formula

S_t = S_{t-1} * exp((mu - 0.5 * sigma^2) * dt + sigma * sqrt(dt) * Z)

- **S0**: current stock price (live via yfinance)
- **mu**: expected annual return (derived from 2y historical daily returns)
- **sigma**: annual volatility (derived from 2y historical daily returns)
- **dt**: 1/252 (one trading day as a fraction of a year)
- **Z**: random shock drawn from a standard normal distribution

## Strengths

- Simple and interpretable implementation
- Guarantees positive stock prices (a property of the exponential function)
- Captures market randomness through Brownian motion
- Generates multiple future price paths, enabling a probabilistic view of outcomes

## Limitations

- Assumes constant volatility over time
- Assumes constant expected return over time
- Models continuous price movement — does not account for sudden crashes or market shocks
- Assumes normally distributed returns, which understates the probability of extreme events

## Analysis

A GBM simulator is only as good as its inputs. The model relies on assumptions — constant mu and sigma, normally distributed returns, continuous movement — that do not always hold in real markets. That said, GBM remains a foundational tool in quantitative finance precisely because it is tractable and interpretable. Rather than predicting a single outcome, it produces a distribution of possible futures, giving the viewer a probabilistic sense of where a stock price may go. It is best understood as a framework for thinking about risk and uncertainty, not a precise forecasting tool.

## How to Run

1. Clone the repo
2. Install dependencies: pip install numpy matplotlib yfinance
3. Run: python Nvidia_GBM_Stock_Stimulator.py

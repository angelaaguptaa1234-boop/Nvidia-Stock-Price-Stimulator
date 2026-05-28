# Nvidia Stock Price Simulator

Built using Geometric Brownian Motion, this Monte Carlo stock price simulator is fed real market data and predicts the trajectory of Nvidia's stock price over 1 trading year. It simulates 100 possible paths the stock may take over the course of the year using historical data from the past 2 years.

## The Formula

S_t = S_{t-1} * exp((mu - 0.5 * sigma^2) * dt + sigma * sqrt(dt) * Z)

- **S0**: current stock price (live via yfinance)
- **mu**: expected annual return (calculated from 2y historical data)
- **sigma**: annual volatility (calculated from 2y historical data)
- **dt**: 1/252 (one trading day as fraction of year)
- **Z**: random shock from standard normal distribution

## Strengths

- Simple and easy to implement
- Realistic (only produces positive stock prices)
- Captures the market's randomness using Brownian motion
- Predicts multiple future stock prices, allowing for a more comprehensive view of possible outcomes

## Weaknesses

- Assumes constant volatility
- Assumes constant expected return
- Assumes continuous movement, ignoring potential crashes or market booms
- Assumes normal distribution of returns

## Overall Analysis

A GBM stock simulator is fed various inputs which are all assumptions. These assumptions take away from the accuracy of the model. However, this does not mean the model is not useful — it can visually show the different paths a stock may go through, giving a holistic view of projected growth. The GBM model is not meant to be perfectly accurate, rather it provides a relatively good grasp of the trajectory the stock price is likely to go through.

## How to Run

1. Clone the repo
2. Install used libraries: pip install numpy matplotlib yfinance
3. Run: python Nvidia_GBM_Stock_Stimulator.py

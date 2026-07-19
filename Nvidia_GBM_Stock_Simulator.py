# importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# specifying the ticker
ticker = yf.Ticker("NVDA")

# THE PARAMETERS
# building the parameters for the model
# these are inputs (assumptions that are fed to the model)

# the current stock value (starting)
S0 = ticker.history(period="5d")["Close"].iloc[-1]
# mu = the annual expected return
# averaging daily returns then scaling it up to annual to determine mu
# calculating daily returns than scaling it up because of law of large numbers
data = yf.Ticker("NVDA").history(period="2y")["Close"]
daily_returns = data.pct_change().dropna()
mu = daily_returns.mean()*252
# sigma = annual volatility
# standard deviations of daily returns (day to day price fluctuation)
sigma = daily_returns.std()*np.sqrt(252)
# T = the amount of time into the future the model predicts
T = 1
# dt = size of one time step within the model (one day)
dt = 1/252
# n_simulations = number of different simulations
n_simulations = 1,000

# THE MODEL SET UP

# fixing the randomness
np.random.seed(123)
# calculating the total steps (days to get to T)
n_steps = int(T/dt)
# creating an empty grid to store predicted prices
prices = np.zeros ((n_steps, n_simulations))
# filling the first row of the grid with the S0 (the current stock price)
prices[0]= S0

# THE DAILY PREDICTIONS (using a loop)
for t in range(1, n_steps):
    # Z = a random number from a standard deviation the provides "the shock"
    Z = np.random.standard_normal(n_simulations)
    # GMB stock stimulator formula
    prices[t] = prices[t-1] * np.exp((mu-0.5 * sigma ** 2) * dt  + sigma * np.sqrt(dt)*Z)

# THE PLOT
plt.plot(prices, alpha = 0.5)
plt.title("NVDA GBM stock price simulation with 100 paths")
plt.xlabel("Trading days")
plt.ylabel("Stock price ($)")
#draws a horizontal dashed line at the intial (current) stock price
plt.axhline(y=S0, color ="black", linestyle ="--", label= "Start: $"+str(S0))
plt.legend()
plt.tight_layout()
plt.show()

# Printing out model inputs
print("GBM model inputs:")
print("Current stock price (S0) =", S0)
print("Expected annual return (mu) =", mu)
print("Expected annual volatility (sigma) =", sigma)
print("Time horizon (T) =", T)
print("The size of each time step (dt) =", dt)
print("Number of simulations =", n_simulations)

print()

# Printing average, max and min stock price
print("Average final price: $" + str(round(prices[-1].mean(), 2)))
print("Min final price: $" + str(round(prices[-1].min(),2)))
print("Max final price: $" + str(round(prices[-1].max(),2)))










import argparse

import numpy as np
import matplotlib.pyplot as plt

def plot_ratios(ratios):
    x = np.arange(ratios.size)

    plt.plot(x, ratios)
    plt.xscale('log')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Plot the ratios between Fibonacci numbers')
    parser.add_argument('n', type=int, help='The number of Fibonacci numbers to calculate')
    args = parser.parse_args()

    ratios = fibonacci_ratios(args.n)
    ratios = np.array(ratios, dtype=np.float64)
    plot_ratios(ratios)

if __name__ == '__main__':
    main()

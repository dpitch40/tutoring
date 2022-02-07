import argparse

import numpy as np
import matplotlib.pyplot as plt

def plot_ratios(ratios):
    x = np.arange(ratios.size)

    plt.plot(x, ratios)
    plt.xscale('log')
    plt.show()
    

def fibonacci_ratios(itterations):
    fibs = [1, 1]
    
    for i in range(itterations - 2):
        fibs.append(fibs[i] + fibs[i + 1])

    fib_ratios = [fibs[i + 1] / fibs[i] for i in range(itterations - 1)]

    return fib_ratios

def main():
    #parser = argparse.ArgumentParser(description='Plot the ratios between Fibonacci numbers')
    #parser.add_argument('n', type=int, help='The number of Fibonacci numbers to calculate')
    #args = parser.parse_args()
    
    ratios = fibonacci_ratios(70)
    ratios = np.array(ratios, dtype=np.float64)
    plot_ratios(ratios)

if __name__ == '__main__':
    main()

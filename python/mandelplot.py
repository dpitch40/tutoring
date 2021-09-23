"""python3 mandelplot.py -n 40 -1.795 -1.74 -0.03 0.03 -r 0.00005
"""

import argparse

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

DEFAULT_RESOLUTION = 0.001
DEFAULT_ITERATIONS = 30
DEFAULT_BOUNDS = [-2, 1, -1, 1]
MAGNITUDE_THRESHOLD = 2

def mandelplot(x, y, iterations=DEFAULT_ITERATIONS):
    # Initialize some arrays
    # Generate initial c values
    c = np.zeros((y.size, x.size), dtype=np.cdouble)
    c += x.reshape((1, x.size))
    c -= y.reshape((y.size, 1)) * 1j

    # Generate array to store current z values
    z = np.zeros_like(c)
    # Generate output array (showing iterations to escape)
    output = np.zeros_like(c, dtype=np.int32)
    # Array for keeping track of which points have escaped
    escaped = np.zeros_like(c, dtype=np.bool_)
    for iteration in range(iterations):
        # Only iterate on poitns that haven't escaped yet
        in_bounds = ~escaped
        compute_indices = np.nonzero(in_bounds)
        # Perform the iteration on z
        z[compute_indices] **= 2
        z[compute_indices] += c[compute_indices]
        magnitudes = np.absolute(z)
        # Check which points exceed the magnitude threshold (are escaping)
        escaping = magnitudes > MAGNITUDE_THRESHOLD
        escaping_indices = np.nonzero(escaping & in_bounds)
        # Set output and escaped for these points
        output[escaping_indices] = iteration
        escaped[escaping_indices] = True

    return output

def main():
    parser = argparse.ArgumentParser(description='Generate a plot of the Mandelbrot set')
    parser.add_argument('bounds', nargs='*', type=float)
    parser.add_argument('-r', '--resolution', default=DEFAULT_RESOLUTION, type=float)
    parser.add_argument('-n', '--iterations', default=DEFAULT_ITERATIONS, type=int)
    args = parser.parse_args()

    figure = plt.figure(dpi=150)
    axes = plt.axes()
    np.random.seed(19680801)
    if args.bounds and len(args.bounds) == 4:
        xmin, xmax, ymin, ymax = args.bounds
    else:
        xmin, xmax, ymin, ymax = DEFAULT_BOUNDS
    x = np.arange(xmin, xmax+args.resolution, args.resolution)
    y = np.arange(ymin, ymax+args.resolution, args.resolution)
    z = mandelplot(x, y, args.iterations)

    axes.pcolormesh(x, y, z, shading='auto')
    plt.show()

if __name__ == '__main__':
    main()

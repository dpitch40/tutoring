"""python3 mandelplot.py -n 40 -1.795 -1.74 -0.03 0.03 -r 0.00005
"""

import argparse

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib.widgets import Slider

DEFAULT_RESOLUTION = 0.001
DEFAULT_ITERATIONS = 30
DEFAULT_BOUNDS = [-2, 1, -1, 1]
MAGNITUDE_THRESHOLD = 2
MAX_ITERATIONS = 1000

class Mandelplot:
    def __init__(self, axes):
        self.axes = axes
        self.last_iterations = None

    def plot(self, xmin, xmax, ymin, ymax, iterations):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.iterations = iterations

        x, y, z = self.calculate()
        self.axes.pcolormesh(x, y, z, shading='auto')
        plt.show()

    def replot(self):
        xmin, xmax = self.axes.get_xlim()
        ymin, ymax = self.axes.get_ylim()
        if xmin != self.xmin:
            self.xmin = xmin
        if xmax != self.xmax:
            self.xmax = xmax
        if ymin != self.ymin:
            self.ymin = ymin
        if ymax != self.ymax:
            self.ymax = ymax

        x, y, z = self.calculate()
        self.axes.clear()
        self.axes.pcolormesh(x, y, z, shading='auto')
        plt.draw()

    def calculate(self):
        width, height = get_size(self.axes)
        # Initialize some arrays
        x = np.linspace(self.xmin, self.xmax, width)
        y = np.linspace(self.ymin, self.ymax, height)
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
        for iteration in range(self.iterations):
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

        self.last_iterations = self.iterations

        return x, y, output

def get_size(axes):
    bbox = axes.get_window_extent()
    return int(bbox.width), int(bbox.height)


def main():
    parser = argparse.ArgumentParser(description='Generate a plot of the Mandelbrot set')
    parser.add_argument('bounds', nargs='*', type=float)
    args = parser.parse_args()

    if args.bounds and len(args.bounds) == 4:
        xmin, xmax, ymin, ymax = args.bounds
    else:
        xmin, xmax, ymin, ymax = DEFAULT_BOUNDS

    figure, axes = plt.subplots(dpi=150)

    # adjust the main plot to make room for the sliders
    plt.subplots_adjust(bottom=0.25)

    axiter = plt.axes([0.25, 0.1, 0.65, 0.03])
    slider = Slider(
        ax=axiter,
        label='Iterations', valmin=1, valmax=MAX_ITERATIONS,
        valstep=np.arange(1, MAX_ITERATIONS+1), valinit=DEFAULT_ITERATIONS,
    )

    # Define event handlers
    def update(val):
        mandelplot.iterations = slider.val
    slider.on_changed(update)

    def onrelease(event):
        if mandelplot.last_iterations != mandelplot.iterations:
            mandelplot.replot()
    cid = figure.canvas.mpl_connect('button_release_event', onrelease)

    release_zoom = NavigationToolbar2.release_zoom
    def on_release_zoom(self, event):
        release_zoom(self, event)
        mandelplot.replot()
    NavigationToolbar2.release_zoom = on_release_zoom

    mandelplot = Mandelplot(axes)
    mandelplot.plot(xmin, xmax, ymin, ymax, DEFAULT_ITERATIONS)

if __name__ == '__main__':
    main()

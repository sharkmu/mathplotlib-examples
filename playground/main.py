import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

def line_diagram():
    plt.plot(xpoints, ypoints)
    plt.show()

line_diagram()

def line_diagram_o():
    plt.plot(xpoints, ypoints, 'o')
    plt.show()

line_diagram_o()

def line_diagram_marker():
    plt.plot(xpoints, ypoints, marker='x') # You can also use 'o' etc.
    plt.show()

line_diagram_marker()
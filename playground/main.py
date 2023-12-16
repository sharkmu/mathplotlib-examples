import matplotlib.pyplot as plt
import numpy as np

def line_diagram():
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    plt.plot(xpoints, ypoints)
    plt.show()

line_diagram()
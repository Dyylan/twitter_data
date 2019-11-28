import matplotlib.pyplot as plt 
import numpy as np

def time_plot_scatter_1d(datetimes, y_offset=0):
    plt.plot(datetimes, np.zeros_like(datetimes) + y_offset, 'x')
    plt.show()



import matplotlib.pyplot as plt
import numpy as np

def animate(x,y):
    fig, axs = plt.subplots()
    axs.plot(x,y)
    plt.show()
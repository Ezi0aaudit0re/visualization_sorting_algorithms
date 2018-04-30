"""
    This file is a wrapper for matplotlib library and is used to create graphs

"""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time
from constants import *

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
arr = list()
colors = ['b' for i in range(ARRAY_SIZE)]


"""
    This function is used to animate the graph i.e for sorting arrays
"""
def animate(i):
    # if arr == None:
    #     # our animation is completed
    #     time.sleep(5)
    #     plt.close()
    #     return

    ids = [key for key, value in enumerate(arr)]
    ax1.clear()
    ax1.bar(ids, arr, color=colors)


"""
    This method plots the graph 
    THis method runs in the main thread
"""
def plot(title):
    ani = animation.FuncAnimation(fig, animate, interval=2)
    print(title)
    plt.title("{}\n".format(title))
    plt.show()


"""
    At every itteration of sorting this function is called to set the values
    
"""
def set_arr(arr_value, color_location=0, previos_color_location=0):
    global arr, colors
    arr = arr_value
    colors[color_location] = "r"
    if previos_color_location >= 0:
        colors[previos_color_location] = "b"






"""
    THis file consists of various sorting algorithms
"""

__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

from matplotlib_wrapper import *
import threading
import random
import time # to see how much time taken
from constants import *

arr = [random.randint(RAND_MIN, RAND_MAX) for _ in range(ARRAY_SIZE)]
worst_case_arr = [i for i in range(ARRAY_SIZE, 1, -1)]
sorted_arr = [i for i in range(ARRAY_SIZE)]
ids = range(0, ARRAY_SIZE)






"""
    Insertion sort
    :param: list to sort
"""
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        set_arr(arr, i, i-1)
        time.sleep(.01)

    # set array value to none after sorting completed
    set_arr(arr) # set the arr as the final array value
    # set_arr(None)


if __name__  == "__main__":
    main()

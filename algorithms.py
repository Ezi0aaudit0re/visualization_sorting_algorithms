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
        time.sleep(SLEEP_TIME)

    # set array value to none after sorting completed
    set_arr(arr) # set the arr as the final array value
    # set_arr(None)




"""
    Interface for quicksort algo
"""
def quick_sort(arr):
    quicksort(arr, 0, len(arr) - 1)


"""
    This is the recrusive part of quicksort method
    :param: arr -> The array to sort
    :param: start -> the lower value
    :param: end -> the higher value
"""


def quicksort(arr, start=0, end=len(arr) - 1):
    par = 0
    if start < end:
        # if more than one element in the list to be sorted

        # call partition function and divide list into two parts
        par = partition(arr, start, end)
        quicksort(arr, start, par-1)
        quicksort(arr, par+1, end)
        set_arr(arr)
        time.sleep(SLEEP_TIME + 0.03)
    else:
        set_arr(arr, par, par-1)


"""
    This function is called to calculate the pivot of the quick sort algo
"""
def get_pivot(arr, low, high):
    mid = (low + high) // 2
    pivot = high

    # calulate the median of teh pivot
    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            pivot = mid
    elif arr[low] < arr[high]:
        pivot = low
    return pivot





"""
    This function is called to take care of the partition side of the qick sort method
"""
def partition(arr, start, end):
    pivot_index = get_pivot(arr, start, end)
    pivot = arr[pivot_index]

    arr[pivot_index], arr[start] = arr[start], arr[pivot_index]
    border = start

    for i in range(start, end+1):

        if arr[i] < pivot:
            # each time we swap an item we move the border to the right by one space
            border = border + 1
            arr[i], arr[border] = arr[border], arr[i]

    arr[start], arr[border] = arr[border], arr[start]

    return border



################################## MEREGE SORT ################################


"""
    This function is the interface for our sorting algorithm
"""
def merge_sort(arr):
    mergesort_algo(arr, 0, len(arr) -1 )


"""
    This function does the breaking part of the algorithm
"""
def mergesort_algo(arr, first, last):
    if first < last:
        # this checks if there is more than 1 item in the list

        # break into two sub arrays
        middle = (first + last) // 2

        # recursively call the algo on the sub problems
        mergesort_algo(arr, first, middle)
        mergesort_algo(arr, middle + 1, last)

        set_arr(arr)
        time.sleep(SLEEP_TIME)
        # we finally merge the subarrays
        merge(arr, first, middle+1, last)
        set_arr(arr)






def merge(arr, first, middle, last):

    # we copy the left half and the right half in two seprate variables
    left_half, right_half = arr[first:middle], arr[middle: last+1]

    # append a value to the end of both the list so that we know we have reached the end of the list
    left_half.append(999999999)
    right_half.append(999999999)


    # index for both of the list
    i = j = 0

    for k in range(first, last + 1):

        if left_half[i] is not None and left_half[i] <= right_half[j]:
            # if the left element is smaller we copy the left element in the list
            # and then increment the index into that list
            arr[k] = left_half[i]
            i = i + 1

        elif right_half[j] is not None and right_half[j] <= left_half[i]:
            # we copy the RIGHT element in the list
            # and we increment the RIGHT INDEX
            arr[k] = right_half[j]
            j = j+1






if __name__ == "__main__":
    arr = [3, 4, 2, 6, 7, 5, 1, 10, 9]
    quick_sort(arr)
    print(arr)




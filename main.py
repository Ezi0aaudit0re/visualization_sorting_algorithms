"""
    THis file is the driver of the program
"""

__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"


from algorithms import *


def main():
    thread1 = threading.Thread(target=insertion_sort, args=(worst_case_arr,))
    # set the valueus for the graph
    thread2 = threading.Thread(target=plt.bar, args=(ids, arr))

    thread1.start()
    thread2.start()

    # we plot in the main  thread
    plot()


if __name__ == "__main__":
    main()
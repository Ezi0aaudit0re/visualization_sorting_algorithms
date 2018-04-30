"""
    THis file is the driver of the program
"""

__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"


from algorithms import *
import sys


arr = [random.randint(RAND_MIN, RAND_MAX) for _ in range(ARRAY_SIZE)]
worst_case_arr = [i for i in range(ARRAY_SIZE, 1, -1)]
sorted_arr = [i for i in range(ARRAY_SIZE)]


def main():
    if(len(sys.argv) == 3):
        algo, case = get_algo_and_case()
    else:
        algo, case = (quick_sort, arr)
    thread1 = threading.Thread(target=algo, args=(case,))
    # set the valueus for the graph
    thread2 = threading.Thread(target=plt.bar, args=(case, arr))

    thread1.start()
    thread2.start()

    # we plot in the main  thread
    plot()



def get_algo_and_case():

    case = sys.argv[2]
    algo = sys.argv[1]

    # set algorithms
    if algo == 0:
        algo= insertion_sort
    elif algo == 1:
        algo = merge_sort(arr)
    elif algo == 2:
        algo = quicksort
    else:
        algo = merge_sort


    # check for cases
    if case == 0:
        case =  arr
    elif case == 1:
        case = worst_case_arr
    elif case == 2:
        case = sorted_arr
    else:
        case = arr


    return (algo, case)


if __name__ == "__main__":
    main()
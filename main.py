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
    if(len(sys.argv) >= 2):
        algo, case = get_algo_and_case()
        title = get_title(algo)
    else:
        print("Please specify an algorithm to run")
        exit(1)

    thread1 = threading.Thread(target=algo, args=(case,))
    # set the valueus for the graph
    thread2 = threading.Thread(target=plt.bar, args=(case, arr))

    thread1.start()
    thread2.start()

    # we plot in the main  thread
    plot(title)



def get_algo_and_case():

    # we will get defalt case of arr and insertion sort
    case = sys.argv[2] if len(sys.argv) == 3 else 0
    algo = sys.argv[1] if sys.argv[1] else 0
    algo, case = int(algo), int(case)


    # set algorithms
    if algo == 0:
        algo= insertion_sort
    elif algo == 1:
        algo = merge_sort
    elif algo == 2:
        algo = quick_sort
    elif algo == 3:
        algo = max_heap_sort
    else:
        algo = merge_sort


    # check for cases
    if case == 0:
        case = arr
    elif case == 1:
        case = worst_case_arr
    elif case == 2:
        case = sorted_arr
    else:
        case = arr


    return (algo, case)


def get_title(algo):
    if algo == insertion_sort:
        return "Insertion Sort"
    elif algo == quick_sort:
        return "QUICK SORT"
    elif algo == merge_sort:
        return "MERGE SORT"
    elif algo == max_heap_sort:
        return "MAX HEAP SORT"


if __name__ == "__main__":
    main()
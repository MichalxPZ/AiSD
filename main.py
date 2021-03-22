from sorts import *
from plots import plots
from runFiles import runFiles

def main():
    TESTSAMOUNT = 1
    MAX_RANGE = 1000
    INPUT_SIZE = [50, 100, 200, 300, 500, 1000]
    SORTS_LIST = {
                  selectionSort: "select_sort",
                  insertionSort: "insert_sort",
                  bubbleSort: "bubble_sort",
                  quickSort: "quick_sort",
                  mergeSort: "merge_sort",
                  heapSort: "heap_sort",
                  countingSort: "counting_sort"
    }
    #runFiles(TESTS=TESTS, MAX_RANGE=MAX_RANGE, INPUT_SIZE = INPUT_SIZE, SORTS_LIST=SORTS_LIST)
    plots(SORTS_LIST=SORTS_LIST, INPUT_SIZE=INPUT_SIZE, TESTSAMOUNT=TESTSAMOUNT)


if __name__ == '__main__':
    main()

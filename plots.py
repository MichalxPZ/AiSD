from statistics import fmean
import time
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from matplotlib import pyplot as plt

from testsForPlot import *

TESTS = [
         random1,
         constValue,
         ascendingOrder,
         descendingOrder,
         shapeA,
         shapeV
         ]

def plots(SORTS_LIST, INPUT_SIZE, TESTSAMOUNT):
    for algo in SORTS_LIST:
        for test in TESTS:
            test_input = INPUT_SIZE
            if algo != selectionSort and algo != insertionSort and algo != bubbleSort and test_input.count(100000)==0 and test_input.count(1000000)==0:
                test_input.append(list(range(10000, 1000000, 50)))
            y = []
            for size in test_input:
                start = time.time()*100
                test(algo, size)
                end = time.time()*100
                t = end-start
                print(test.__name__, str(size), str(t))
                y.append(float(t))
            x = np.array(test_input).reshape((-1, 1))
            y = np.array(y)
            model = LinearRegression().fit(x, y)
            y_pred = []
            x_pred = []
            for i in range(0, max(test_input), max(test_input)//100):
                x_pred.append(i)
                y_pred.append(model.intercept_ + model.coef_ * i)
            plt.plot(x_pred, y_pred, label=test.__name__)
        plt.legend()
        plt.xlabel("Input size [n]")
        plt.ylabel("Time [ms]")
        plt.title(SORTS_LIST[algo])
        plt.savefig("plot{}.png".format(algo.__name__))
        plt.clf()


if __name__ == '__main__':
    TESTSAMOUNT = 1
    MAX_RANGE = 1000
    INPUT_SIZE = list(range(50, 10000, 50))
    SORTS_LIST = {
         selectionSort: "select_sort",
         insertionSort: "insert_sort",
         bubbleSort: "bubble_sort",
         quickSort: "quick_sort",
         mergeSort: "merge_sort",
         heapSort: "heap_sort",
         countingSort: "counting_sort"
    }
    plots(SORTS_LIST, INPUT_SIZE, 1)

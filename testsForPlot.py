from sorts import *

algos = [selectionSort, insertionSort, bubbleSort, quickSort, mergeSort, heapSort, countingSort]

def random1(algo, LENGHT):
    tab = [0] * LENGHT
    for i in range(LENGHT):
        tab[i] = randint(0, 100)
    return algo(tab)


def random2(algo, LENGHT):
    tab = [0] * LENGHT
    for i in range(LENGHT):
        tab[i] = randint(0, 100)
    return algo(tab)


def random3(algo, LENGHT):
    tab = [0] * LENGHT
    for i in range(LENGHT):
        tab[i] = randint(0, 100)
    return algo(tab)


def constValue(algo, LENGHT):
    tab = [0] * LENGHT
    const_val = randint(1, 5)
    for i in range(LENGHT):
        tab[i] = const_val
    return algo(tab)


def descendingOrder(algo, LENGHT):
    tab = [0] * LENGHT
    for i in range(LENGHT):
        tab[i] = randint(0, 200)
    tab = sorted(tab, reverse=True)
    return algo(tab)


def ascendingOrder(algo, LENGHT):
    tab = [0] * LENGHT
    for i in range(LENGHT):
        tab[i] = randint(0, 200)
    tab = sorted(tab)
    return algo(tab)


def shapeA(algo, LENGHT):
    tab = [0] * LENGHT
    for i in range(LENGHT):
        tab[i] = randint(0, 200)
    half1 = sorted(tab[0:len(tab) // 2])
    half2 = sorted(tab[(len(tab) // 2) + 1::], reverse=True)
    tab = half1 + half2
    return algo(tab)


def shapeV(algo, LENGHT):
    tab = [0] * LENGHT
    for i in range(LENGHT):
        tab[i] = randint(0, 200)
    half1 = sorted(tab[0:len(tab) // 2], reverse=True)
    half2 = sorted(tab[(len(tab) // 2) + 1::])
    tab = half1 + half2
    return algo(tab)

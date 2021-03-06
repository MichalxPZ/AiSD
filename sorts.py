import time
from random import randint
#from random import shuffle


# def bogoSort(numbers):
#     srtNums = sorted(numbers)
#     while numbers != srtNums:
#         shuffle(numbers)
#     return numbers


def selectionSort(numbers):
    for i in range(len(numbers)):
        index_min = i
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[index_min]:
                index_min = j
        numbers[index_min], numbers[i] = numbers[i], numbers[index_min]
    return numbers


def insertionSort(numbers):
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[j] > numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def bubbleSort(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def quickSort(numbers):
    tabMore = []
    tabEqual = []
    tabLess = []
    if len(numbers) > 1:
        pivot = numbers[randint(0, len(numbers)-1)]
        for i in range(len(numbers)):
            if numbers[i] > pivot:
                tabMore.append(numbers[i])
            elif numbers[i] < pivot:
                tabLess.append(numbers[i])
            else:
                tabEqual.append(pivot)
        return quickSort(tabLess) + tabEqual + quickSort(tabMore)
    else:
        return numbers


def mergeSort(numbers):
    if len(numbers) > 1:
        numbers1 = numbers[:len(numbers)//2]
        numbers2 = numbers[len(numbers)//2:]
        numbers1 = mergeSort(numbers1)
        numbers2 = mergeSort(numbers2)

        k, i, j = 0, 0, 0
        while i < len(numbers1) and j < len(numbers2):
            if numbers1[i] < numbers2[j]:
                numbers[k] = numbers1[i]
                i += 1
            else:
                numbers[k] = numbers2[j]
                j += 1
            k += 1
    return numbers


def heapSort(numbers):
    def heapify(numbers, parentIndex):
        largestValueIndex = parentIndex
        firstChildIndex = 2 * parentIndex + 1
        secondChildIndex = 2 * parentIndex + 2
        if len(numbers) > firstChildIndex and numbers[largestValueIndex] < numbers[firstChildIndex]:
            largestValueIndex = firstChildIndex
            numbers[largestValueIndex], numbers[firstChildIndex] = numbers[firstChildIndex], numbers[largestValueIndex]
        if len(numbers) > secondChildIndex and numbers[largestValueIndex] < numbers[secondChildIndex]:
            largestValueIndex = secondChildIndex
            numbers[largestValueIndex], numbers[secondChildIndex] = numbers[secondChildIndex], numbers[largestValueIndex]
        return numbers

    for i in range(len(numbers)//2 - 1, -1, -1):
        numbers = heapify(numbers, i)
    return numbers


def countingSort(numbers):
    tab = [0] * (max(numbers) + 1)
    for i in numbers:
        tab[i] += 1
    numbers = []
    for i in range(len(tab)):
        for j in range(tab[i]):
            numbers.append(i)
    return numbers


def main():
    sorts = [selectionSort, insertionSort, bubbleSort, quickSort, mergeSort, heapSort, countingSort]
    f = open("Values/selectionSort_values1000_32.txt")
    tab = list(map(int, f.readline().strip().split(", ")))
    print(tab)
    for sort in sorts:
        start = time.time()
        print("{}: {}".format(sort.__name__, sort(tab)))
        end = time.time()
        t = end - start
        print("Time: {}".format(str(t)))


if __name__ == '__main__':
    main()

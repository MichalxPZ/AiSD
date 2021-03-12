import unittest
import sorts
from random import randint

class MyTestCase(unittest.TestCase):
    def testRandom1(self):
        tabLenght = randint(1, 1000)
        tab = [0] * tabLenght
        for i in range(tabLenght):
            tab[i] = randint(0, 1000)
        tabSort = sorted(tab)
        self.assertEqual(sorts.selectionSort(tab), tabSort)
        self.assertEqual(sorts.insertionSort(tab), tabSort)
        self.assertEqual(sorts.bubbleSort(tab), tabSort)
        self.assertEqual(sorts.quickSort(tab), tabSort)
        self.assertEqual(sorts.mergeSort(tab), tabSort)
        self.assertEqual(sorts.heapSort(tab), tabSort)
        self.assertEqual(sorts.countingSort(tab), tabSort)


    def testRandom2(self):
        tabLenght = randint(1, 500)
        tab = [0] * tabLenght
        for i in range(tabLenght):
            tab[i] = randint(0, 1000)
        tabSort = sorted(tab)
        self.assertEqual(sorts.selectionSort(tab), tabSort)
        self.assertEqual(sorts.insertionSort(tab), tabSort)
        self.assertEqual(sorts.bubbleSort(tab), tabSort)
        self.assertEqual(sorts.quickSort(tab), tabSort)
        self.assertEqual(sorts.mergeSort(tab), tabSort)
        self.assertEqual(sorts.heapSort(tab), tabSort)
        self.assertEqual(sorts.countingSort(tab), tabSort)


    def testRandom3(self):
        tabLenght = randint(1, 10000)
        tab = [0] * tabLenght
        for i in range(tabLenght):
            tab[i] = randint(0, 200)
        tabSort = sorted(tab)
        self.assertEqual(sorts.selectionSort(tab), tabSort)
        self.assertEqual(sorts.insertionSort(tab), tabSort)
        self.assertEqual(sorts.bubbleSort(tab), tabSort)
        self.assertEqual(sorts.quickSort(tab), tabSort)
        self.assertEqual(sorts.mergeSort(tab), tabSort)
        self.assertEqual(sorts.heapSort(tab), tabSort)
        self.assertEqual(sorts.countingSort(tab), tabSort)


    def testConstValue(self):
        tabLenght = randint(1, 1000)
        tab = [0] * tabLenght
        const_val = randint(1, 5)
        for i in range(tabLenght):
            tab[i] = const_val
        tabSort = sorted(tab)
        self.assertEqual(sorts.selectionSort(tab), tabSort)
        self.assertEqual(sorts.insertionSort(tab), tabSort)
        self.assertEqual(sorts.bubbleSort(tab), tabSort)
        self.assertEqual(sorts.quickSort(tab), tabSort)
        self.assertEqual(sorts.mergeSort(tab), tabSort)
        self.assertEqual(sorts.heapSort(tab), tabSort)
        self.assertEqual(sorts.countingSort(tab), tabSort)


    def testAscendingOrder(self):
        tabLenght = randint(1, 10000)
        tab = [0] * tabLenght
        for i in range(tabLenght):
            tab[i] = randint(0, 200)
        tab = sorted(tab, reverse=True)
        tabSort = sorted(tab)
        self.assertEqual(sorts.selectionSort(tab), tabSort)
        self.assertEqual(sorts.insertionSort(tab), tabSort)
        self.assertEqual(sorts.bubbleSort(tab), tabSort)
        self.assertEqual(sorts.quickSort(tab), tabSort)
        self.assertEqual(sorts.mergeSort(tab), tabSort)
        self.assertEqual(sorts.heapSort(tab), tabSort)
        self.assertEqual(sorts.countingSort(tab), tabSort)


    def testDescendingOrder(self):
        tabLenght = randint(1, 10000)
        tab = [0] * tabLenght
        for i in range(tabLenght):
            tab[i] = randint(0, 200)
        tab = sorted(tab)
        tabSort = sorted(tab)
        self.assertEqual(sorts.selectionSort(tab), tabSort)
        self.assertEqual(sorts.insertionSort(tab), tabSort)
        self.assertEqual(sorts.bubbleSort(tab), tabSort)
        self.assertEqual(sorts.quickSort(tab), tabSort)
        self.assertEqual(sorts.mergeSort(tab), tabSort)
        self.assertEqual(sorts.heapSort(tab), tabSort)
        self.assertEqual(sorts.countingSort(tab), tabSort)


    def testPyramid(self):
        tabLenght = randint(1, 10000)
        tab = [0] * tabLenght
        for i in range(tabLenght):
            tab[i] = randint(0, 200)
        half1 = sorted(tab[0:len(tab)//2])
        half2 = sorted(tab[(len(tab)//2) + 1 ::], reverse=True)
        tab = half1 + half2
        tabSort = sorted(tab)
        self.assertEqual(sorts.selectionSort(tab), tabSort)
        self.assertEqual(sorts.insertionSort(tab), tabSort)
        self.assertEqual(sorts.bubbleSort(tab), tabSort)
        self.assertEqual(sorts.quickSort(tab), tabSort)
        self.assertEqual(sorts.mergeSort(tab), tabSort)
        self.assertEqual(sorts.heapSort(tab), tabSort)
        self.assertEqual(sorts.countingSort(tab), tabSort)


if __name__ == '__main__':
    unittest.main()

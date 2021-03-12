# AiSD
Sprawozdania Algorytmy i Struktury Danych, PUT Informatyka, semestr II


Algorytmy sortowania
Politechnika Poznańska
Informatyka, semestr II
Algorytmy i Struktury Danych
Michał Zieliński 
INF5.1 148064


Wszystkie implementacje algorytmów, testy jednostkowe i kod generujący wykres jest dostępny w repozytorium pod poniższym linkiem:
https://github.com/MichalxPZ/AiSD


Cel sprawozdania:
zaimplementowanie podstawowych algorytmów sortowania w języku Python
przetestowanie algorytmów
porównanie złożoności czasowej algorytmów

Algorytmy:
Selection Sort
Insertion Sort
Bubble Sort
Quick Sort
Merge Sort
Heap Sort
Counting Sort


Selection Sort
Opis:
Algorytm przegląda tablicę n razy i za każdym razem umieszcza najmniejszy element na początku. Sortowanie w miejscu. Algorytm niestabilny. Złożoność czasowa O(n^2)
Implementacja:

```
def selectionSort(numbers):
    for i in range(len(numbers)):
        index_min = i
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[index_min]:
                index_min = j
        numbers[index_min], numbers[i] = numbers[i], numbers[index_min]
    return numbers
```












Insertion Sort
Opis:
 Algorytm wstawia kolejne elementy zbioru nieposortowanego na odpowiednie miejsce w zbiorze posortowanym. Sortowanie w miejscu. Algorytm stabilny. Złożoność czasowa O(n^2). Najgorszy przypadek to taki, gdy elementy są posortowane w kolejności malejącej.
Implementacja:
```
def insertionSort(numbers):
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[j] > numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers
```


Bubble Sort
Opis:
Algorytm przechodzi po kolejnych indeksach tablicy. Porównuje dwa sąsiednie elementy i zamienia jeśli są w złej kolejności. Sortowanie w miejscu. Algorytm stabilny. Złożoność czasowa: najgorszy i średni przypadek O(n^2), najlepszy przypadek O(n)
Implementacja:
```
def bubbleSort(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

```

















Quick Sort
Opis:
Podejście dziel i zwyciężaj. Algorytm wybiera pivot jako losowy element z tablicy i dzieli ją na dwie podtablice. W pierwszej umieszczamy elementy większe od pivota, a w drugiej mniejsze. Wywołujemy algorytm rekurencyjnie na podtablicach aż do momentu, gdy długość tablicy będzie mniejsza bądź równa 1. Złożoność czasowa w średnim przypadku to O(n*logn), a w najgorszym przypadku, gdy algorytm zawsze wybierze najmniejszy lub największy element za pivot O(n^2).
Implementacja:
```
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

```
Merge Sort
Opis:
Podejście dziel i zwyciężaj. Algorytm dzieli tablicę na pół rekurencyjnie, aż do uzyskania podtablic o długości jeden, które są posortowane. Następnie od ostatniego wywołania funkcji łączymy dwie posortowane podtablice w jedną która jest wynikiem tego wywołania. Algorytm stabilny. Złożoność pamięciowa O(n), złożoność czasowa O(n*logn).
Implementacja:
```
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

```
Heap Sort
Opis:
Algorytm bazuje na strukturze kopca.
Elementy rodzice (indeks k) mają dzieci o indeksach 2k+! i 2k+2
Najpierw funkcja heapify() rozpatruje rodzica i dzieci i zamienia ich miejscami w ten sposób, że w korzeniu poddrzewa znajduje się element o największej wartości.
Funkcja ta jest wykonywana na wszystkich rodzicach od ostatniego.
Kopiec się rozrasta i elementy ustawiają się na odpowiednich miejscach.
Sortowanie w miejscu. Złożoność pamięciowa to O(n), a czasowa O(n*logn)
Implementacja:
```
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
```
Counting Sort
Opis:
Algorytm stosuje dodatkową tablicę pomocniczą, która zlicza ilość wystąpień każdego elementu. Następnie elementy są zwracane. Złożoność czasowa i pamięciowa to O(n + k).
Implementacja:
```
def countingSort(numbers):
    tab = [0] * (max(numbers) + 1)
    for i in numbers:
        tab[i] += 1
    numbers = []
    for i in range(len(tab)):
        for j in range(tab[i]):
            numbers.append(i)
    return numbers
```
Testy poprawności algorytmów
Do sprawdzenia działania algorytmów zastosowałem testy jednostkowe.
Trzy pierwsze testy wygenerowałem za pomocą liczb pseudolosowych. Są to tablice o losowej długości z zakresu 1 - 10000 z liczbami z zakresu 0-1000.
Test czwarty jest to sprawdzenie algorytmu dla stałej wartości dla wszystkich elementów.
Test piąty i szósty są to liczby posortowane rosnąco i malejąco.
Ostatni test jest to “piramida”, gdzie pierwsza połowa tablicy jest posortowana rosnąco, a druga malejąco.
Poniżej umieszczam tylko implementację testu dla piramidy.
Reszta testów jest dostępna w repozytorium github.
import unittest
import sorts
from random import randint
```
class MyTestCase(unittest.TestCase):
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
```

Porównanie złożoności algorytmów
Tworzę po 100 testów dla każdej wielkości danych [50, 100, 200, 300, 500, 1000]
Test zapełniam liczbami pseudolosowymi z zakresu 0-1000.
Wywołuję funkcje sortowania dla każdego pliku wejściowego i zapisuję wynik oraz czas plikach wyjściowych. Czas mierzę za pomocą biblioteki time.



main.py
```
from sorts import *
from plots import plots
from runFiles import runFiles

def main():
    TESTS = 100
    MAX_RANGE = 1000
    INPUT_SIZE = [50, 100, 200, 300, 500, 1000]
    SORTS_LIST = {selectionSort: "select_sort",
                  insertionSort: "insert_sort",
                  bubbleSort: "bubble_sort",
                  quickSort: "quick_sort",
                  mergeSort: "merge_sort",
                  heapSort: "heap_sort",
                  countingSort: "counting_sort"}
    runFiles(TESTS=TESTS, MAX_RANGE=MAX_RANGE, INPUT_SIZE = INPUT_SIZE, SORTS_LIST=SORTS_LIST)
    plots(SORTS_LIST=SORTS_LIST, INPUT_SIZE=INPUT_SIZE, TESTS=TESTS)


if __name__ == '__main__':
    main()
```

runFiles.py
```
from random import randint
from time import time
def runFiles(SORTS_LIST, INPUT_SIZE, TESTS, MAX_RANGE):
    for func in SORTS_LIST.keys():
        for size in INPUT_SIZE:
            for i in range(1, TESTS + 1):
                value_file_name = "{}_values{}_{}.txt".format(func.__name__, str(size), str(i))
                result_file_name = "{}_results{}_{}.txt".format(func.__name__, str(size), str(i))
                time_file_name = "{}_time{}_{}.txt".format(func.__name__, str(size), str(i))
                f = open("Values/" + value_file_name, 'w')
                for j in range(1, size + 1):
                    f.write(str(randint(0, MAX_RANGE)))
                    f.write(" ")
                f.close()
                f = open("Results/" + result_file_name, 'w')
                t = open("Times/" + time_file_name, 'w')
                r = open("Values/" + value_file_name, 'r')
                inputArray = list(map(int, r.readline().strip().split(" ")))
                start = time()
                results = func(inputArray)
                end = time()
                times = (end - start)*1000
                for j in range(1, size):
                    f.write(str(results[j]))
                    f.write(" ")
                t.write(str(times))
                f.close()
                t.close()
                r.close()
```
Zestawienie wyników na wykresie
Stworzyłem wykres za pomocą biblioteki matplotlib. I zestawiłem na nim średni czas sortowania danych przez dany algorytm w zależności od wielkości danych wejściowych.

plots.py
```
from matplotlib import pyplot as plt
from statistics import fmean


def plots(SORTS_LIST, INPUT_SIZE, TESTS):
    dictOfPlotPoints = {}
    for algo in SORTS_LIST.keys():
        y_avg_time = []
        for size in INPUT_SIZE:
            y_times = []
            for i in range(1, TESTS + 1):
                time_file_name = "{}_time{}_{}.txt".format(algo.__name__, str(size), str(i))
                f = open("Times/" + time_file_name, "r")
                y_times.append(float(f.readline()))
            y_avg_time.append(fmean(y_times))
        dictOfPlotPoints[algo] = {"x": INPUT_SIZE, "y": y_avg_time}
        plt.plot(dictOfPlotPoints[algo]["x"], dictOfPlotPoints[algo]["y"], label=str(SORTS_LIST[algo]))
    plt.legend()
    plt.axis(xmax=1100, ymin=0, ymax=40)
    plt.title("Sorting Algorithms")
    plt.xlabel('input size [n]')
    plt.ylabel("time [ms]")
    plt.savefig("plot.pdf")
```
Wygenerowany został poniższy wykres:

  plot.pdf


Wnioski
W moim przypadku najgorszą efektywnością wykazał się algorytm Bubble Sort
Niewiele gorzej również wypadły Insert Sort oraz Select Sort.
Są to wszystkie algorytmy o średniej złożoności obliczeniowej O(n^2)
Znacznie lepsze rezultaty można zauważyć w algorytmach Quick Sort i Merge Sort, algorytmach reprezentujących podejście dziel i zwyciężaj.
Najlepiej wypadły algorytmy Heap Sort i Counting Sort.


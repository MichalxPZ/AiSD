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
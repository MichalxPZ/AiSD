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
    plt.savefig("plot.png")

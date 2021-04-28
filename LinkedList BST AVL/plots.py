from matplotlib import pyplot as plt

RANGES = [50, 100, 500, 750, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
STRUCTS = {"LinkedList": "LinkedList", "BST": "BST", "AVL": "AVL"}
OPERATIONS = ["tworzenie", "Delete", "Find"]
TESTS = ["Losowe", "Rosnace", "Malejace", "A", "V"]

def main():
    for operation in OPERATIONS:
        for test in TESTS:
            for struct in STRUCTS.keys():
                resultFile = open("txt/" + struct + operation + test + ".txt", "r")
                y = []
                lines = resultFile.read().split("\n")
                for i in range(0, len(lines)-1):
                    y.append(float(lines[i]))
                plt.plot(RANGES, y, label="{}".format(struct))
                resultFile.close()
            plt.legend()
            plt.xlabel("Input size [n]")
            plt.ylabel("Time [ms]")
            plt.title("{} Dane: {}".format(operation.capitalize(), test.capitalize()))
            plt.savefig("plots/plot{}{}.png".format(operation.capitalize(), test.capitalize()))
            plt.clf()


if __name__ == '__main__':
    main()

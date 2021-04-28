from random import randint
import os

RANGES = [50, 100, 500, 750, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
STRUCTS = {"LinkedList": "LinkedList", "BST": "BST", "AVL": "AVL"}

def rosnace():
    for struct in STRUCTS.keys():
        f = open("txt/result.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultFind.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultDelete.txt", "w")
        f.write("")
        f.close()
        for i in RANGES:
            f = open("txt/input.txt", "w")
            f.write("")
            f.close()
            with open("txt/input.txt", "a") as f:
                for j in range(i):
                    f.write("{}\n".format(j))
            os.system("./{}".format(STRUCTS[struct]))
        os.system("cat txt/result.txt > txt/{}tworzenieRosnace.txt".format(struct))
        os.system("cat txt/resultFind.txt > txt/{}FindRosnace.txt".format(struct))
        os.system("cat txt/resultDelete.txt > txt/{}DeleteRosnace.txt".format(struct))


def malejace():
    for struct in STRUCTS.keys():
        f = open("txt/result.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultFind.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultDelete.txt", "w")
        f.write("")
        f.close()
        for i in RANGES:
            f = open("txt/input.txt", "w")
            f.write("")
            f.close()
            with open("txt/input.txt", "a") as f:
                for j in range(i, 0, -1):
                    f.write("{}\n".format(j))
            os.system("./{}".format(STRUCTS[struct]))
        os.system("cat txt/result.txt > txt/{}tworzenieMalejace.txt".format(struct))
        os.system("cat txt/resultFind.txt > txt/{}FindMalejace.txt".format(struct))
        os.system("cat txt/resultDelete.txt > txt/{}DeleteMalejace.txt".format(struct))

def vShape():
    for struct in STRUCTS.keys():
        f = open("txt/result.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultFind.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultDelete.txt", "w")
        f.write("")
        f.close()
        for i in RANGES:
            f = open("txt/input.txt", "w")
            f.write("")
            f.close()
            with open("txt/input.txt", "a") as f:
                for j in range(i, i//2, -1):
                    f.write("{}\n".format(j))
                for j in range(i//2):
                    f.write("{}\n".format(j))
            os.system("./{}".format(STRUCTS[struct]))
        os.system("cat txt/result.txt > txt/{}tworzenieV.txt".format(struct))
        os.system("cat txt/resultFind.txt > txt/{}FindV.txt".format(struct))
        os.system("cat txt/resultDelete.txt > txt/{}DeleteV.txt".format(struct))

def aShape():
    for struct in STRUCTS.keys():
        f = open("txt/result.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultFind.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultDelete.txt", "w")
        f.write("")
        f.close()
        for i in RANGES:
            f = open("txt/input.txt", "w")
            f.write("")
            f.close()
            with open("txt/input.txt", "a") as f:
                for j in range(i//2):
                    f.write("{}\n".format(j))
                for j in range(i, i//2, -1):
                    f.write("{}\n".format(j))
            os.system("./{}".format(STRUCTS[struct]))
        os.system("cat txt/result.txt > txt/{}tworzenieA.txt".format(struct))
        os.system("cat txt/resultFind.txt > txt/{}FindA.txt".format(struct))
        os.system("cat txt/resultDelete.txt > txt/{}DeleteA.txt".format(struct))


def losowe():
    for struct in STRUCTS.keys():
        f = open("txt/result.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultFind.txt", "w")
        f.write("")
        f.close()
        f = open("txt/resultDelete.txt", "w")
        f.write("")
        f.close()
        for i in RANGES:
            f = open("txt/input.txt", "w")
            f.write("")
            f.close()
            with open("txt/input.txt", "a") as f:
                for j in range(i):
                    f.write("{}\n".format(randint(0, 10000)))
            os.system("./{}".format(STRUCTS[struct]))
        os.system("cat txt/result.txt > txt/{}tworzenieLosowe.txt".format(struct))
        os.system("cat txt/resultFind.txt > txt/{}FindLosowe.txt".format(struct))
        os.system("cat txt/resultDelete.txt > txt/{}DeleteLosowe.txt".format(struct))

def main():
    losowe()
    malejace()
    rosnace()
    aShape()
    vShape()

if __name__ == '__main__':
    main()

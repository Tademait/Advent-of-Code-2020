import cProfile


def getVal():
    wanted_val = 2020
    with open("inputs/input1.txt", "r") as f1:
        for first in f1:
            with open("input1.txt", "r") as f2:
                for second in f2:
                    sum = int(first) + int(second)
                    if sum == wanted_val:
                        print(f"the result is: {int(first) * int(second)}")
                        quit(0)


cProfile.run('getVal()')

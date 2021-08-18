wanted_val = 2020
values = []
with open("advent1/input1.txt", "r") as f:
    for line in f.readlines():
        values.append(int(line))
    for first in values:
        for second in values:
            for third in values:
                sum = int(first) + int(second) + int(third)
                if sum == wanted_val:
                    print(f"the result is: {first * second * third}")
                    quit(0)

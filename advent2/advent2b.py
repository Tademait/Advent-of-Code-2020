import re


def checkPassword(pwd):
    try:
        if bool(pwd_data[3][int(pwd_data[0]) - 1] == pwd_data[2])\
                ^ bool(pwd_data[3][int(pwd_data[1]) - 1] == pwd_data[2]):
            return 1
        else:
            return 0
    except IndexError:
        return 0


correct_pwds_counter = 0
with open("advent2/input.txt", "r") as f:
    values = f.readlines()
for item in values:
    pwd_data = re.split(r':\s|\n|[-\s]', item)
    correct_pwds_counter += checkPassword(pwd_data)
print(f"The number of valid passwords is: {correct_pwds_counter}")

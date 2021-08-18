import re

values = []
correct_pwds_counter = 0
with open("advent2/input.txt", "r") as f:
    for line in f:
        values.append(line)
for item in values:
    pwd_data = re.split(r':\s|\n|[-\s]', item)
    char_counter = 0
    for char in pwd_data[3]:
        if char == pwd_data[2]:
            char_counter += 1
    if int(pwd_data[0]) <= char_counter <= int(pwd_data[1]):
        correct_pwds_counter += 1
print(f"The number of valid passwords is: {correct_pwds_counter}")

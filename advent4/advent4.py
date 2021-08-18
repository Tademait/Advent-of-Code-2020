import re


def checkPassportValid(passport):
    required_info = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    for info in required_info:
        if info in passport:
            continue
        else:
            return False
    return True


passport = []
valid_passports = 0
with open("advent4/input.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            if checkPassportValid(passport):
                valid_passports += 1
            passport = []
        else:
            split_line = re.split(r'[:\s]', line)
            for item in split_line:
                if item == '':
                    continue
                passport.append(item)
print(f"The number of valid passports is: {valid_passports}")

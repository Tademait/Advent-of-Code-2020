import re


def correct_id(string):
    if string[-1] == "0":
        return False
    return True


def correct_colorcode(string):
    for char in string:
        if char in "abcdef0123456789":
            continue
        else:
            return False
    return True


def list_to_dict(passport):
    it = iter(passport)
    res_dct = dict(zip(it, it))
    return res_dct


def checkPassportValid(passport):
    required_info = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    pass_dict = list_to_dict(passport)
    for key in required_info:
        if key == "byr":
            if key in pass_dict and len(pass_dict[key]) == 4 and 1920 <= int(pass_dict[key]) <= 2002:
                continue
        if key == "iyr":
            if key in pass_dict and len(pass_dict[key]) == 4 and 2010 <= int(pass_dict[key]) <= 2020:
                continue
        if key == "eyr":
            if key in pass_dict and len(pass_dict[key]) == 4 and 2020 <= int(pass_dict[key]) <= 2030:
                continue
        if key == "hgt":
            if key in pass_dict and pass_dict[key][-2:] == "cm" and 150 <= int(pass_dict[key][:-2]) <= 193:
                continue
            if key in pass_dict and pass_dict[key][-2:] == "in" and 59 <= int(pass_dict[key][:-2]) <= 76:
                continue
        if key == "hcl":
            if key in pass_dict and pass_dict[key][0] == "#" and correct_colorcode(pass_dict[key][1:]):
                continue
        if key == "ecl":
            eye_options = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            if key in pass_dict and pass_dict[key] in eye_options:
                continue
        if key == "pid":
            if key in pass_dict and len(pass_dict[key]) == 9 and correct_id(pass_dict[key]):
                continue
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

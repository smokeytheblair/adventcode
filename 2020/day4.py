import sys
import argparse
import math
from collections import Counter
from operator import xor

reset_report = None

valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def load_inputs(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        report = list(input_file)

        if reset_report is None:
            reset_report = report.copy()

    return report

def convert_to_dicts(passports):
    new_passports = []
    new_passport = dict()

    for passport in passports:
        elements = passport.split()
        for element in elements:
            values = element.split(":")
            new_passport[values[0]] = values[1]

        new_passports.append(new_passport)
        new_passport = dict()

    return new_passports

     
def load_passports(passports_file):
    passports = []

    passport = None
    for line in passports_file:
        if line == "\n" and passport is not None:
            passports.append(passport)
            passport = None
        elif passport is None:
            passport = line[:-1]
        else:
            passport += " " + line[:-1]

    if passport is not None:
        passports.append(passport)

    passports = convert_to_dicts(passports)

    print(f"Loaded {len(passports)} passports from the input.")
    
    return passports

def is_valid_passport(passport):
#    print(passport)

    if passport.get("byr", None) is None:
        return False
    if passport.get("iyr", None) is None:
        return False
    if passport.get("eyr", None) is None:
        return False
    if passport.get("hgt", None) is None:
        return False
    if passport.get("hcl", None) is None:
        return False
    if passport.get("ecl", None) is None:
        return False
    if passport.get("pid", None) is None:
        return False

    return True

def is_valid_passport_strict(passport):
#    print(passport)

    if passport.get("byr", None) is None:
        return False
    else:
        value = int(passport["byr"])
        if value < 1920 or value > 2002:
            return False

    if passport.get("iyr", None) is None:
        return False
    else:
        value = int(passport["iyr"])
        if value < 2010 or value > 2020:
            return False

    if passport.get("eyr", None) is None:
        return False
    else:
        value = int(passport["eyr"])
        if value < 2020 or value > 2030:
            return False

    if passport.get("hgt", None) is None:
        return False
    else:
        unit_type = passport["hgt"][-2:]
        unit_value = int(passport["hgt"][:-2])
        if unit_type == "cm":
            if unit_value < 150 or unit_value > 193:
                return False
        elif unit_type == "in":
            if unit_value < 59 or unit_value > 76:
                return False
        else:
            return False

    if passport.get("hcl", None) is None:
        return False
    elif passport["hcl"][0] != "#":
        return False
    else:
        color = passport["hcl"][1:]
        if len(color) != 6 or color.isalnum() is False:
            return False
        
    if passport.get("ecl", None) is None:
        return False
    elif passport["ecl"] not in valid_colors:
        return False

    if passport.get("pid", None) is None:
        return False
    elif not passport["pid"].isnumeric() or len(passport["pid"]) != 9:
        return False

    return True

def count_passports_1(input_file):
    passports = load_inputs(input_file)
    passports = load_passports(passports)
    
#    print(passports)
    valid_passports = 0

    for passport in passports:
        if is_valid_passport(passport) is True:
            valid_passports += 1

    print(f"Number of valid passports: {valid_passports}")
    return valid_passports

def count_passports_2(input_file):
    passports = load_inputs(input_file)
    passports = load_passports(passports)
    
#    print(passports)
    valid_passports = 0

    for passport in passports:
        if is_valid_passport_strict(passport) is True:
            valid_passports += 1

    print(f"Number of valid passports: {valid_passports}")
    return valid_passports

def main():
    parser = argparse.ArgumentParser(description="Count passports.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                count_passports_1(input_file)
            elif args.part == 2:
                count_passports_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


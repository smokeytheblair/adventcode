import sys
import argparse
import math
import itertools

reset_report = None

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def load_inputs(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        for line in input_file:
            report.append(int(line[:-1])) #remove \n

        if reset_report is None:
            reset_report = report.copy()

    return report

def reduced(permutations):
    reduced_permutations = []

    bookmarked_idx = 0
    for index in range(len(permutations)):
        if index + 2 >= len(permutations):
            reduced_permutations.append(1)
        else:
            check_list = permutations[index:index+3]
            print(f"check_list {check_list}")
            if math.prod(check_list) == 8:
                reduced_permutations.append(7)
                bookmarked_idx = index + 3
            elif index >= bookmarked_idx: 
                reduced_permutations.append(permutations[index])


    return reduced_permutations

def part_1(input_file):
    chargers = sorted(load_inputs(input_file))
#    print(chargers[-1:])
    chargers.append(chargers[-1:][0] + 3)
#    print(chargers)

    counts = [0, 0, 0, 0]
    last_joltage = 0
    for index in range(len(chargers)):
        if chargers[index] - last_joltage <= 3:
            counts[chargers[index] - last_joltage] += 1
        else:
            print("ERROR: joltage gap greater than 3")

        last_joltage = chargers[index]

    print(counts)
    print(f"{counts[1]} * {counts[3]} = {counts[1]*counts[3]}")

def part_2(input_file):
    chargers = sorted(load_inputs(input_file))
    phone_charger = chargers[-1:][0] + 3
    chargers.append(phone_charger)
    print(chargers)

    count = 1    
    counts = [0, 0, 0, 0]
    permutations = []
    last_joltage = 0
    last_last_joltage = 0
    for index in range(len(chargers)):
        if chargers[index] - last_joltage == 3:
            counts[chargers[index] - last_joltage] += 1
            permutations.append(1)
        elif chargers[index] - last_joltage == 1:
            counts[chargers[index] - last_joltage] += 1
            if last_joltage - last_last_joltage == 1:
                permutations.append(2)
            if last_joltage - last_last_joltage == 1:
                count *= 2
        else:
            # print("ERROR: joltage gap greater than 3")
            break

        last_last_joltage = last_joltage
        last_joltage = chargers[index]

    print(f"permutations {permutations}")
    permutations = reduced(permutations)
    print(f"pruned {permutations}")

    print(f"count of numberic gaps = {counts}")            
    print(f"count of sub_sets = {math.prod(permutations)}")

def main():
    parser = argparse.ArgumentParser(description="Compute joltage gaps.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                part_1(input_file)
            elif args.part == 2:
                part_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


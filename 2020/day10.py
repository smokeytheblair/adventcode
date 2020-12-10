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
#    print(chargers[-1:])

    count = 0    
    for set_size in range(len(chargers)//3, len(chargers)+1):
        print(f"set_size = {set_size}")
        sub_chargers = itertools.combinations(chargers, set_size)
        counts = [0, 0, 0, 0]
        for sub in sub_chargers:
            sub = sorted(sub)
            sub.append(phone_charger)
            sub = sorted(sub)
            good_sequence = True
            last_joltage = 0
            for index in range(len(sub)):
                if sub[index] - last_joltage <= 3:
                    counts[sub[index] - last_joltage] += 1
                else:
                    good_sequence = False
                    # print("ERROR: joltage gap greater than 3")
                    break

                last_joltage = sub[index]

            if good_sequence == True:
                print(f"testing sub set: {sub}")
                count += 1

            
    print(f"count of sub_sets = {count}")

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


import sys
import argparse
import math
from collections import defaultdict

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
            report.append(line[:-1])

        if reset_report is None:
            reset_report = report.copy()

    return report

def part_1(input_file):
    rules = load_inputs(input_file)
    
#    print(rules)

    counts = []
    for rule in rules:
        print(rule)

def part_2(input_file):
    pass

def main():
    parser = argparse.ArgumentParser(description="Figure luggage rules.")
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


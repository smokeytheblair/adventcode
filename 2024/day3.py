import sys
import argparse
from idlelib.configdialog import is_int
import re

reset_report = None


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


def part1(input_file):
    inputs = load_inputs(input_file)
    total_result = 0

    for input in inputs:
        print(input)

        muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)
        print(muls)

        for mul in muls:
            nums = re.findall(r'\d+', mul)
            total_result += int(nums[0])*int(nums[1])

    print(f"Total result: {total_result}")


def part2(input_file):
    inputs = load_inputs(input_file)
    total_result = 0

    do_dont = True
    for input in inputs:
        print(input)

        muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', input)
        print(muls)

        for mul in muls:
            if mul == 'do()':
                do_dont = True
            elif mul == 'don\'t()':
                do_dont = False
            elif do_dont:
                nums = re.findall(r'\d+', mul)
                total_result += int(nums[0])*int(nums[1])

    print(f"Total result: {total_result}")

def main():
    parser = argparse.ArgumentParser(description="Advent of Code.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='--part=1 or --part=2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                part1(input_file)
            elif args.part == 2:
                part2(input_file)


if __name__ == "__main__":
    main()


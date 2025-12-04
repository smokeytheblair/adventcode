import itertools
import sys
import argparse

reset_report = None


def load_inputs(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        report = [ str(x).strip() for x in list(input_file)]

        if reset_report is None:
            reset_report = report.copy()

    return report


def part1(input_file):
    inputs = load_inputs(input_file)

    highest_joltage = []

    for line in inputs:
        print(line)
        pairs = itertools.combinations(line, 2)
        highest_num = 0

        for pair in pairs:
            # print(f"pair: {pair}")
            num = int(pair[0] + pair[1])
            highest_num = max(highest_num, num)

        print(f"highest_num: {highest_num}")
        highest_joltage.append(highest_num)

    print(f"highest_joltage: {highest_joltage}")
    print(f"sum: {sum(highest_joltage)}")

def part2(input_file):
    inputs = load_inputs(input_file)


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


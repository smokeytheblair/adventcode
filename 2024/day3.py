import sys
import argparse
from idlelib.configdialog import is_int

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

    values = []

    index = inputs[0].find("mul(")

    while -1 < index:
        # print(f"found at {index} - {inputs[0][index:index+10]}")
        # find valid mul operator
        comma = inputs[0].find(",", index+4)
        close_paren = inputs[0].find(")", index+4)
        val1 = inputs[0][index+4:comma]
        val2 = inputs[0][comma+1:close_paren]

        if is_int(val1) and is_int(val2):
            values.append((int(val1), int(val2)))
            print(f"ADDED val1: {val1}, val2: {val2}")
        else:
            print(f"SKIPPED val1:{val1}, val2: {val2}")

        # remove current and step to the next
        inputs[0] = inputs[0][index+4:]
        index = inputs[0].find("mul(")

    print(f"found values: {values}")

    total_result = 0
    for mul in values:
        total_result += mul[0] * mul[1]

    print(f"Total result: {total_result}")


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


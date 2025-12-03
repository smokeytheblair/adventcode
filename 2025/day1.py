import sys
import argparse

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
    dial_position = 50
    count_zeros = 0
    dial_size = 100

    for instruction in inputs:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == 'R':
            dial_position += distance
            dial_position %= dial_size
            if dial_position == 0:
                count_zeros += 1
        elif direction == 'L':
            dial_position -= distance
            dial_position %= dial_size
            if dial_position == 0:
                count_zeros += 1

        print(f"count_zeros = {count_zeros}")

        print(f"direction: {direction}, distance: {distance}")


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


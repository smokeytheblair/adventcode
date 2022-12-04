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


def find_subsets(input_file):
    assignments = load_inputs(input_file)

    subsets = 0
    for assignment in assignments:
        first, second = assignment.split(',')
        # print(f"{first}, {second}")

        x1, x2 = [int(x) for x in first.split('-')]
        y1, y2 = [int(y) for y in second.split('-')]
        # print(f"{x1}-{x2}, {y1}-{y2}")

        if x1 <= y1 and x2 >= y2:
            subsets += 1
        elif y1 <= x1 and y2 >= x2:
            subsets += 1

    print(f"subsets = {subsets}")


def count_overlaps(input_file):
    assignments = load_inputs(input_file)

    overlaps = 0
    for assignment in assignments:
        first, second = assignment.split(',')
        # print(f"{first}, {second}")

        x1, x2 = [int(x) for x in first.split('-')]
        y1, y2 = [int(y) for y in second.split('-')]
        # print(f"{x1}-{x2}, {y1}-{y2}")

        # first contains second
        if x1 <= y1 and x2 >= y2:
            # overlaps += y2 - y1 + 1
            overlaps += 1
        # second contains first
        elif y1 <= x1 and y2 >= x2:
            # overlaps += x2 - x1 + 1
            overlaps += 1
        elif x2 >= y1 and x1 < y2:
            # overlaps += x2 - y1 + 1
            overlaps += 1
        elif y2 >= x1 and y1 < x2:
            # overlaps += y2 - x1 + 1
            overlaps += 1

    print(f"overlaps = {overlaps}")


def main():
    parser = argparse.ArgumentParser(description="Day 4 part 1 & 2")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                find_subsets(input_file)
            elif args.part == 2:
                count_overlaps(input_file)


if __name__ == "__main__":
    main()


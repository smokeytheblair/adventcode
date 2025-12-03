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


def create_ranges(inputs):
    ranges = []

    for line in inputs:
        range_pairs = line.split(',')

        for range_pair_str in range_pairs:
            range_pair = range_pair_str.split('-')
            ranges.append((range_pair[0], range_pair[1]))

        print(ranges)

    return ranges


def part1(input_file):
    inputs = load_inputs(input_file)

    ranges = create_ranges(inputs)

    invalid_ids = []

    for range_pair in ranges:
        print(range_pair)
        for x in range(int(range_pair[0]), int(range_pair[1])+1):
            num_str = str(x)
            for y in range(len(num_str), (len(num_str)//2)-1, -1):
                # print(f"y: {y}, num_str: {num_str}, sub_str: {num_str[:y]}")
                if len(num_str)%2 == 1:
                    continue
                if num_str.find(num_str[:y], y) == y :
                    print(f"adding {x} to invalid_ids list")
                    invalid_ids.append(x)
                    break

    print(f"invalid_ids: {invalid_ids}")
    print(f"sum: {sum(invalid_ids)}")


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


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


def find_lowest_index(list1, count):
    sorted_list = sorted(list1)
    smallest = sorted_list[count]

    return smallest


def find_total_distance(list1, list2):
    total_distance = 0
    for i in range(len(list1)):
        pos1 = find_lowest_index(list1, i)
        pos2 = find_lowest_index(list2, i)

        print(f"distance[{i}] = {abs(pos1-pos2)} = {pos1}-{pos2}")

        total_distance += abs(pos1 - pos2)

    print(f"Total distance = {total_distance}")


def part1(input_file):
    inputs = load_inputs(input_file)

    print(inputs)

    list1 = []
    list2 = []
    index = 0
    for row in inputs:
        vals = [int(x) for x in row.strip().split("   ")]

        list1.append(vals[0])
        list2.append(vals[1])

    print(f"list1 = {list1}, list2 = {list2}")

    find_total_distance(list1, list2)

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


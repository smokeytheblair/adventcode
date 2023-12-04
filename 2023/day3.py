import sys
import argparse
import numpy

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


def isValidPos(x, y, m, n):
    if x < 0 or y < 0 or x > n - 1 or y > m - 1:
        return False
    return True


def is_symbol(inputs, x, y, m, n):
    if x<0 or y<0:
        return False
    if x>=m or y>=n:
        return False

    if inputs[y][x] in ['!', '@', '#', '$', '%', '&', '*', '=', '+', '-', '/']:
        return True


def is_part_num(inputs, x, y, m, n):
    if not inputs[y][x].isdigit():
        return False

    if is_symbol(inputs, x-1, y, m, n):
        return True
    if is_symbol(inputs, x+1, y, m, n):
        return True
    if is_symbol(inputs, x, y-1, m, n):
        return True
    if is_symbol(inputs, x, y+1, m, n):
        return True
    if is_symbol(inputs, x-1, y-1, m, n):
        return True
    if is_symbol(inputs, x-1, y+1, m, n):
        return True
    if is_symbol(inputs, x+1, y-1, m, n):
        return True
    if is_symbol(inputs, x+1, y+1, m, n):
        return True

    return False


def get_part_num(inputs, x, y, m, n):
    row = inputs[y].strip()

    x_start = x
    for new_x in range(x-1, -1, -1):
        if str(row[new_x]).isdigit():
            x_start = new_x
        else:
            break

    x_end = x
    for new_x in range(x+1,m):
        if str(row[new_x]).isdigit():
            x_end = new_x
        else:
            break

    return int(row[x_start:x_end+1])


def part1(input_file):
    inputs = load_inputs(input_file)

    print(inputs)

    n = len(inputs)
    m = len(inputs[0].strip())

    part_nums = []
    for y in range(len(inputs)):
        same_number = False
        for x in range(len(inputs[y].strip())):
            character = inputs[y][x]
            if not character.isdigit():
                same_number = False
            if not same_number and is_part_num(inputs, int(x), int(y), m, n):
                print(f'inputs[{x}, {y}]: part number {get_part_num(inputs, int(x), int(y), m, n)}')
                part_nums.append(get_part_num(inputs, int(x), int(y), m, n))
                same_number = True

    print(part_nums)
    print(sum(part_nums))


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


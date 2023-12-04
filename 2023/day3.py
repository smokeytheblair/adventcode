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

    return int(row[x_start:x_end+1]), [[x,y] for x in range(x_start, x_end+1)]


def part1(input_file):
    inputs = load_inputs(input_file)

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
                part_nums.append(get_part_num(inputs, int(x), int(y), m, n)[0])
                same_number = True

    print(part_nums)
    print(sum(part_nums))


def find_operand(inputs, x, y, m, n, ops, visited_coords):
    if str(inputs[y][x]).isdigit():
        part_num = []
        if [x, y] not in visited_coords:
            part_num = get_part_num(inputs, x, y, m, n)
            ops.append(part_num[0])
        if len(part_num) == 2:
            for coord in part_num[1]:
                visited_coords.append(coord)

def find_operands(inputs, x, y, m, n):
    ops = []
    visited_coords = []

    # print(f'find_operands[{x}][{y}]')

    if y < n - 1:
        x_temp = x
        y_temp = y + 1
        find_operand(inputs, x_temp, y_temp, m, n, ops, visited_coords)
    if y > 0:
        x_temp = x
        y_temp = y - 1
        find_operand(inputs, x_temp, y_temp, m, n, ops, visited_coords)
    if y < n - 1 and x < m - 1:
        x_temp = x + 1
        y_temp = y + 1
        find_operand(inputs, x_temp, y_temp, m, n, ops, visited_coords)
    if y < n - 1 and x > 0:
        x_temp = x - 1
        y_temp = y + 1
        find_operand(inputs, x_temp, y_temp, m, n, ops, visited_coords)
    if y > 0 and x > 0:
        x_temp = x - 1
        y_temp = y - 1
        find_operand(inputs, x_temp, y_temp, m, n, ops, visited_coords)
    if y > 0 and x < m - 1:
        x_temp = x + 1
        y_temp = y - 1
        find_operand(inputs, x_temp, y_temp, m, n, ops, visited_coords)
    if x > 0:
        x_temp = x - 1
        y_temp = y
        find_operand(inputs, x_temp, y_temp, m, n, ops, visited_coords)
    if x < m - 1:
        x_temp = x + 1
        y_temp = y
        find_operand(inputs, x_temp, y_temp, m, n, ops, visited_coords)

    if len(ops) != 2:
        # print(f'find_operands[{x}][{y}] returning False, 0, 0')
        return False, 0, 0
    else:
        print(f'find_operands[{x}][{y}] returning True {ops[0]}, {ops[1]}')
        return True, ops[0], ops[1]


def part2(input_file):
    inputs = load_inputs(input_file)

    gear = '*'
    n = len(inputs)
    m = len(inputs[0].strip())

    gear_ratios = []
    for y in range(len(inputs)):
        for x in range(len(inputs[y].strip())):
            character = inputs[y][x]
            if character == gear:
                operands = find_operands(inputs, x, y, m, n)
                if operands[0]:
                    gear_ratios.append(operands[1] * operands[2])

    print(gear_ratios)
    print(sum(gear_ratios))



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


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


def next_permutation(operators):
    if '+' not in operators:
        return None

    # least = len(operators) - 1
    # if operators[least] == '+':
    #     operators[least] = '*'
    # else:
    #     operators[least] = '+'

    countdown = list(range(len(operators)-1, -1, -1))
    change_needed = True
    for i in countdown:
        if operators[i] == '+' and change_needed:
            operators[i] = '*'
            change_needed = False
        elif operators[i] == '*' and change_needed:
            operators[i] = '+'
            change_needed = True

    # print(f"operators: {operators}")
    return operators


def next_permutation2(operators):
    if '+' not in operators and '*' not in operators:
        return None

    # least = len(operators) - 1
    # if operators[least] == '+':
    #     operators[least] = '*'
    # else:
    #     operators[least] = '+'

    countdown = list(range(len(operators)-1, -1, -1))
    change_needed = True
    for i in countdown:
        if operators[i] == '+' and change_needed:
            operators[i] = '*'
            change_needed = False
        elif operators[i] == '*' and change_needed:
            operators[i] = '||'
            change_needed = False
        elif operators[i] == '||' and change_needed:
            operators[i] = '+'
            change_needed = True

    # print(f"operators: {operators}")
    return operators


def can_be_true(result, operands):
    operators = ['+' for i in range(len(operands)-1)]

    while True:
        ret = 0
        temp_ops = operands.copy()
        for i in range(len(operators)):
            if '+' == operators[i]:
                temp_ops[i+1] = temp_ops[i] + temp_ops[i+1]
            elif '*' == operators[i]:
                temp_ops[i+1] = temp_ops[i] * temp_ops[i+1]

            ret = temp_ops[i+1]

        if result == ret:
            print(f"can_be_true({result}, {operands}) -> {result}")
            return result
        else:
            operators = next_permutation(operators)
            if operators is None:
                break

    print(f"can_be_true({result}, {operands}) -> 0")
    return 0


def can_be_true2(result, operands):
    operators = ['+' for i in range(len(operands)-1)]

    while True:
        ret = 0
        temp_ops = operands.copy()
        for i in range(len(operators)):
            if '+' == operators[i]:
                temp_ops[i+1] = temp_ops[i] + temp_ops[i+1]
            elif '*' == operators[i]:
                temp_ops[i+1] = temp_ops[i] * temp_ops[i+1]
            elif '||' == operators[i]:
                temp_ops[i+1] = int(str(temp_ops[i]) + str(temp_ops[i+1]))

            ret = temp_ops[i+1]

        if result == ret:
            print(f"can_be_true({result}, {operands}) -> {result}")
            return result
        else:
            operators = next_permutation2(operators)
            if operators is None:
                break

    print(f"can_be_true({result}, {operands}) -> 0")
    return 0


def part1(input_file):
    inputs = load_inputs(input_file)

    total_sum = 0

    for line in inputs:
        result_index = line.find(":")
        result = int(line[:result_index:])
        operands = [int(x) for x in line[result_index+1::].strip().split(" ")]
        print(f"result: {result}, operands: {operands}")

        total_sum += can_be_true(result, operands)

    print(f"total_sum: {total_sum}")


def part2(input_file):
    inputs = load_inputs(input_file)

    total_sum = 0

    for line in inputs:
        result_index = line.find(":")
        result = int(line[:result_index:])
        operands = [int(x) for x in line[result_index+1::].strip().split(" ")]
        print(f"result: {result}, operands: {operands}")

        total_sum += can_be_true2(result, operands)

    print(f"total_sum: {total_sum}")

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


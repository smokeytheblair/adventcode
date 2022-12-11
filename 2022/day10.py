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

    reg_X = 1
    exec_history = [1]
    cycles = 0
    for instruction in inputs:
        command = instruction.split(' ')
        cmd = command[0].strip()

        if 'noop' == cmd:
            cycles += 1
            exec_history.append(reg_X)
        elif 'addx' == cmd:
            exec_history.append(reg_X)
            reg_X += int(command[1].strip())
            exec_history.append(reg_X)
            cycles += 2

    print(f"register X: {reg_X}, cycles: {cycles}")
    print(f"execution history: {exec_history}")

    signals = []
    for cycle in range(19, len(exec_history), 40):
        value = exec_history[cycle]
        signals.append((cycle+1) * value)

    print(f"signal sum: {sum(signals)}")


def part2(input_file):
    inputs = load_inputs(input_file)

    reg_X = 1
    exec_history = [1]
    cycles = 1
    row = -1
    screen_output = []

    # set up first row
    MAX_ROW_LEN = 40
    new_row = ''
    screen_output.append(new_row)
    row += 1

    for instruction in inputs:
        command = instruction.split(' ')
        cmd = command[0].strip()

        if 'noop' == cmd:
            if 0 <= ((cycles % MAX_ROW_LEN) - reg_X) <= 2:
                screen_output[row] += '#'
            else:
                screen_output[row] += '.'

            exec_history.append(reg_X)

            cycles += 1

            if len(screen_output[row]) % MAX_ROW_LEN == 0:
                new_row = ''
                screen_output.append(new_row)
                row += 1
        elif 'addx' == cmd:
            if 0 <= ((cycles % MAX_ROW_LEN) - reg_X) <= 2:
                screen_output[row] += '#'
            else:
                screen_output[row] += '.'

            cycles += 1

            if len(screen_output[row]) % MAX_ROW_LEN == 0:
                new_row = ''
                screen_output.append(new_row)
                row += 1

            if 0 <= ((cycles % MAX_ROW_LEN) - reg_X) <= 2:
                screen_output[row] += '#'
            else:
                screen_output[row] += '.'

            exec_history.append(reg_X)
            reg_X += int(command[1].strip())
            exec_history.append(reg_X)

            cycles += 1

            if len(screen_output[row]) % MAX_ROW_LEN == 0:
                new_row = ''
                screen_output.append(new_row)
                row += 1

    # print(f"register X: {reg_X}, cycles: {cycles}")
    # print(f"execution history: {exec_history}")

    signals = []
    for cycle in range(19, len(exec_history), 40):
        value = exec_history[cycle]
        signals.append((cycle+1) * value)

    # print(f"signal sum: {sum(signals)}")

    print(f"screen output:\n{screen_output}")

    for row in screen_output:
        print(row)


def main():
    parser = argparse.ArgumentParser(description="Advent of Code.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                part1(input_file)
            elif args.part == 2:
                part2(input_file)


if __name__ == "__main__":
    main()


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


def report_is_safe_1(numbers):
    up_down = 0

    for i in range(len(numbers)):
        if i+1 < len(numbers):
            if 3 < abs(numbers[i] - numbers[i+1]) or 0 == numbers[i] - numbers[i+1]:
                return False
            if 0 < numbers[i] - numbers[i+1]:
                if up_down >= 0:
                    up_down = 1
                else:
                    return False
            if 0 > numbers[i] - numbers[i+1]:
                if up_down <= 0:
                    up_down = -1
                else:
                    return False

    return True


def check_numbers(val1, val2, up_down):
    if 3 < abs(val1 - val2) or 0 == val1 - val2:
        return False, up_down
    elif 0 < val1 - val2:
        if up_down >= 0:
            up_down = 1
        else:
            return False, up_down
    elif 0 > val1 - val2:
        if up_down <= 0:
            up_down = -1
        else:
            return False, up_down

    return True, up_down


def report_is_safe_2(numbers):
    up_down = 0
    ret = True

    numbers_a = numbers.copy()
    numbers_b = numbers.copy()

    for i in range(len(numbers)):
        if i+1 < len(numbers) and ret:
            ret, up_down = check_numbers(numbers[i], numbers[i+1], up_down)

            if not ret:
                del (numbers_a[i])
                del (numbers_b[i+1])
                break

    if not ret:
        up_down = 0
        ret = True
        for i in range(len(numbers_a)):
            if i+1 < len(numbers_a) and ret:
                ret, up_down = check_numbers(numbers_a[i], numbers_a[i+1], up_down)

                if not ret:
                    break

    if not ret:
        up_down = 0
        ret = True
        for i in range(len(numbers_b)):
            if i+1 < len(numbers_b) and ret:
                ret, up_down = check_numbers(numbers_b[i], numbers_b[i+1], up_down)

                if not ret:
                    break

    return ret


def part1(input_file):
    inputs = load_inputs(input_file)

    safe_reports = 0
    for report in inputs:
        numbers = [int(x) for x in report.strip().split(" ")]

        if report_is_safe_1(numbers):
            safe_reports += 1

    print(f"Safe Reports: {safe_reports}")


def part2(input_file):
    inputs = load_inputs(input_file)

    safe_reports = 0
    for report in inputs:
        numbers = [int(x) for x in report.strip().split(" ")]

        if report_is_safe_2(numbers):
            safe_reports += 1
            print(f"report:{numbers} is SAFE")

    print(f"Safe Reports: {safe_reports}")


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


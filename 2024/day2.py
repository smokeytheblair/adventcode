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

        if report_is_safe_1(numbers):
            safe_reports += 1
            print(f"report:{numbers} is SAFE")
        else:
            found_safe = False
            for i in range(len(numbers)):
                temp_list = numbers.copy()
                del (temp_list[i])
                if report_is_safe_1(temp_list):
                    safe_reports += 1
                    found_safe = True
                    print(f"report:{numbers} is SAFE")
                    break

            if not found_safe:
                print(f"report:{numbers} is NOT safe" )

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


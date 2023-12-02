import sys
import argparse
import re

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

    numbers = []
    sum = 0

    for line in inputs:
        num = ''
        digits = re.findall(r'\d', line)
        print(digits)
        num += digits[0]
        num += digits[-1:][0]

        if len(num) != 0:
            new_num = int(num)
            numbers.append(new_num)
            sum += new_num

    print(f"sum: {sum}, numbers: {numbers}")

def find_digits(line:str):
    digits = []
    digit_words = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    numbers = re.findall(r'\d|zero|one|two|three|four|five|six|seven|eight|nine', line)

    print(numbers)

    for num in numbers:
        if num in digit_words.keys():
            digits.append(digit_words[num])
        else:
            digits.append(num)

    print(digits)

    return digits


def part2(input_file):
    inputs = load_inputs(input_file)

    numbers = []
    sum = 0

    for line in inputs:
        num = ''
        digits = find_digits(line)
        print(digits)
        num += digits[0]
        num += digits[-1:][0]

        if len(num) != 0:
            new_num = int(num)
            numbers.append(new_num)
            sum += new_num

    print(f"sum: {sum}, numbers: {numbers}")


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


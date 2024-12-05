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


def rotate_90(wordsearch):
    print("Rotate table 90 degrees")

    new_wordsearch = []
    for i in range(len(wordsearch[0])):
        new_line = ''
        for j in range(len(wordsearch)):
            new_line += wordsearch[j][i]

        print(new_line)
        new_wordsearch.append(new_line)

    return new_wordsearch


def part1(input_file):
    inputs = load_inputs(input_file)
    wordsearch = []
    for line in inputs:
        print(line.strip())
        wordsearch.append(line.strip())

    print(wordsearch)

    word_count = 0

    for i in range(2):
        for line in wordsearch:
            words = re.findall(r"XMAS|SAMX", line)
            word_count += len(words)

        wordsearch = rotate_90(wordsearch)

    print (f"word_count: {word_count}")


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


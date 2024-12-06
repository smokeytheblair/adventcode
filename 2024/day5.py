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

    precedence = {}
    middle_pages = []
    reading_rules = True
    for line in inputs:
        if 1 < len(line) and reading_rules:
            key, value = [int(x) for x in line.strip().split("|")]
            if None == precedence.get(key):
                precedence[key] = [value]
            else:
                precedence[key].append(value)
        else:
            reading_rules = False
            if "\n" == line:
                continue

            pages = [int(x) for x in line.strip().split(",")]
            good_line = True
            for page in pages:
                if None != precedence.get(page) and good_line:
                    current_page = pages.index(page)
                    for i in range(len(pages)):
                        if pages[i] in precedence[page] and i <= current_page:
                            good_line = False
                            break

            if good_line:
                middle_pages.append(pages[int((len(pages)-1)/2)])

    print(f"Sum: {sum(middle_pages)}, pages: {middle_pages}")





    print(f"precedence: {precedence}")


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


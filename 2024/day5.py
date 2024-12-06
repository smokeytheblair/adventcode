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


def correct_line(pages, precedence):
    new_pages = pages.copy()
    for i in range(len(pages)):
        for key, rules in precedence.items():
            if key in pages and rules is not None:
                current_index = new_pages.index(key)
                for rule in rules:
                    if rule in new_pages:
                        page_index = new_pages.index(rule)
                        if page_index < current_index:
                            new_pages.insert(current_index, new_pages.pop(page_index))

    print(f"correct_line returned: {new_pages}")
    return new_pages


def part2(input_file):
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
            # check each page in the list
            for page in pages:
                # see if this page has precedence rules
                if None != precedence.get(page) and good_line:
                    current_page = pages.index(page)
                    # verify the precedence rules for this page
                    for i in range(len(pages)):
                        # page at index i violates the precedence rules
                        if pages[i] in precedence[page] and i <= current_page:
                            good_line = False
                            # pages.insert(current_page, pages.pop(i))
                            new_pages = correct_line(pages, precedence)

                            # count the corrected lines
                            if not good_line:
                                middle_index = int((len(new_pages)-1)/2)
                                print(f"middle_index: {middle_index}")
                                middle_page = new_pages[middle_index]
                                print(f"adding {middle_page}")
                                middle_pages.append(middle_page)
                                break

    print(f"Sum: {sum(middle_pages)}, pages: {middle_pages}")


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


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


def count_calories(input_file):
    meals = load_inputs(input_file)

    calorie_sums = {}
    elf_num = 0
    for meal in meals:
        if meal == '\n':
            elf_num += 1
            continue

        if None is calorie_sums.get(elf_num):
            calorie_sums[elf_num] = 0

        calorie_sums[elf_num] += int(meal)

    glutton = max(calorie_sums.values())
    print(f"Max calories = {glutton}")

    return calorie_sums


def count_calories_2(input_file):
    meals = load_inputs(input_file)

    calorie_sums = {}
    elf_num = 0
    for meal in meals:
        if meal == '\n':
            elf_num += 1
            continue

        if None is calorie_sums.get(elf_num):
            calorie_sums[elf_num] = 0

        calorie_sums[elf_num] += int(meal)

    print(calorie_sums)

    top_three = list(calorie_sums.values())
    top_tree = top_three.sort()
    print(top_three)
    print(f"top_three = {sum(top_three[-3:])}")


def main():
    parser = argparse.ArgumentParser(description="Count depth increases.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                count_calories(input_file)
            elif args.part == 2:
                count_calories_2(input_file)



if __name__ == "__main__":
    main()


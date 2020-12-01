import sys
import itertools
import argparse

reset_report = None

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def load_expense_report(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        report = list(input_file)

        if reset_report is None:
            reset_report = report.copy()

    return report
     
def process_expense_report(input_file, number):
    report = load_expense_report(input_file)

    if number == 2:
        for num_a, num_b in itertools.combinations(report, number):
            num_1 = int(num_a)
            num_2 = int(num_b)
            if num_1 + num_2 == 2020:
                print(f"{num_1} + {num_2} == {num_1+num_2}\n{num_1} * {num_2} == {num_1 * num_2}")
                break

    if number == 3:
        for num_a, num_b, num_c in itertools.combinations(report, number):
            num_1 = int(num_a)
            num_2 = int(num_b)
            num_3 = int(num_c)
            if num_1 + num_2 + num_3 == 2020:
                print(f"{num_1} + {num_2} + {num_3} == {num_1+num_2+num_3}\n{num_1} * {num_2} * {num_3} == {num_1 * num_2 * num_3}")
                break

def main():
    parser = argparse.ArgumentParser(description='Compute required fuel for modules, or modules+fuel')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--number', type=int, required=True, help='How many nums to add/multiply.')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            process_expense_report(input_file, args.number)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


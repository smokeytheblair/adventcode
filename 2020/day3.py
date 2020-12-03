import sys
import argparse
from collections import Counter
from operator import xor

reset_report = None

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

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
     
def count_trees_1(input_file):
    report = load_inputs(input_file)
#    print(report)
    
    row_index = 0
    num_tree = 0
    for record in report:
        line_len = len(record[:-1])
        print(record)

        if record[row_index] == "#":
            num_tree += 1
            print(f"tree at {row_index}")
        else:
            print(f"no tree at {row_index}")

        row_index = (row_index + 3) % line_len

    print(f"Number of trees: {num_tree}")

def check_passwords_2(input_file):
    report = load_inputs(input_file)
#    print(report)
    
    num_valid = 0
    for record in report:
        print(record)
#        print(count)
        valid = False
        if xor(record[2] == record[3][record[0]-1], record[3][record[1]-1] == record[2]):
            valid = True
            num_valid += 1

        print(f"{record[3]} has {record[2]} in proper slot - VALID = {valid}")

    print(f"Number of valid password: {num_valid}")

def main():
    parser = argparse.ArgumentParser(description="Count trees.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--number', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.number == 1:
                count_trees_1(input_file)
            elif args.number == 2:
                check_passwords_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


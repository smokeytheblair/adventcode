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
     
def convert_tuples(report):
    new_report = []
    for record in report:
        hyphen = record.find('-')
        colon = record.find(':')
        space = record.find(' ')

        min_val = int(record[0:hyphen])
        max_val = int(record[hyphen+1:space])
        letter = record[space+1:colon]
        password = record[colon+2:-1]

        new_report.append( (min_val, max_val, letter, password) )

    return new_report

def check_passwords_1(input_file):
    report = load_inputs(input_file)
#    print(report)
    report = convert_tuples(report)
#    print(report)
    
    num_valid = 0
    for record in report:
        count = Counter(record[3])
        print(record)
#        print(count)
        valid = False
        if record[0] <= count[record[2]] and count[record[2]] <= record[1]:
            valid = True
            num_valid += 1

        print(f"{record[3]} has {count[record[2]]} {record[2]}'s - VALID = {valid}")

    print(f"Number of valid password: {num_valid}")

def check_passwords_2(input_file):
    report = load_inputs(input_file)
#    print(report)
    report = convert_tuples(report)
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
    parser = argparse.ArgumentParser(description='Check passwords')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='How many nums to add/multiply.')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                check_passwords_1(input_file)
            elif args.part == 2:
                check_passwords_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


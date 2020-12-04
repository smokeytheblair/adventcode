import sys
import argparse
import math
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
     
def load_slopes(slopes_file):
    slopes = []

    for slope in slopes_file:
        slopes.append( ( int(slope[0]), int(slope[2]) ) )

    return slopes

def count_trees_1(input_file, run, rise):
    report = load_inputs(input_file)
    
    print(f"Counting trees for slope({run}, {rise})")

    row_index = 0
    num_trees = 0
    col_index = 0
    row_count = 0
    for record in report:
        if 0 != row_count % rise:
            row_count += 1
            continue

#        print(f"Processing row {row_count}")

        line_len = len(record[:-1])
#        print(record)

        if record[row_index] == "#":
            num_trees += 1
#            print(f"tree at [{row_count}][{row_index}]")
#        else:
#            print(f"no tree at [{row_count}][{row_index}]")

        row_index = (row_index + run) % line_len
        row_count += 1

    print(f"Number of trees on slope({run},{rise}): {num_trees}")
    return num_trees

def count_trees_2(input_file, slopes_file):
    slopes = load_slopes(slopes_file)

    counts = []
    for slope in slopes:
        counts.append( count_trees_1(input_file, int(slope[0]), int(slope[1])) )

    print(f"Total number of trees = {math.prod(counts)}")

def main():
    parser = argparse.ArgumentParser(description="Count trees.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')
    parser.add_argument("slopes", type=argparse.FileType('r'))

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                count_trees_1(input_file, 3, 1)
            elif args.paert == 2:
                with args.slopes as slopes_file:
                    count_trees_2(input_file, slopes_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


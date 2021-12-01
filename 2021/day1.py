import sys
import argparse

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

def count_depths(input_file):
    depths = load_inputs(input_file)

    count = 0
    prev_depth = 0
    for depth in depths:
        if 0 != prev_depth and int(depth) > prev_depth:
            count += 1

        prev_depth = int(depth)

    print(f"Count = {count}")
    
def count_depths_2(input_file):
    depths = load_inputs(input_file)

    count = 0
    for index in range(len(depths)):
        if index < len(depths)-3:
            A = int(depths[index]) + int(depths[index+1]) + int(depths[index+2])
            B = int(depths[index+1]) + int(depths[index+2]) + int(depths[index+3])
#            print(f"A = {A} < B = {B}")
            if A < B:
                count += 1
#                print(f"count = {count}")

    print(f"Count = {count}")

def main():
    parser = argparse.ArgumentParser(description="Count depth increases.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                count_depths(input_file)
            elif args.part == 2:
                count_depths_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


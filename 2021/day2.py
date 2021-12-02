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

    tuples = []
    for line in report:
        direction = line.split()
#        print(f"line: {line}, direction: {direction}")
        tuples.append((direction[0], int(direction[1])))

    return tuples

def compute_path(input_file):
    directions = load_inputs(input_file)
#    print(f"{directions}")

    forward = 0
    depth = 0
    for direction in directions:
        if direction[0] == "forward":
            forward += direction[1]
        elif direction[0] == "up":
            depth -= direction[1]
        elif direction[0] == "down":
            depth += direction[1]

    print(f"forward:{forward} * depth:{depth} = {forward*depth}")

    
def compute_path_2(input_file):
    directions = load_inputs(input_file)

    aim = 0
    forward = 0
    depth = 0
    for direction in directions:
        if direction[0] == "forward":
            forward += direction[1]
            depth += aim * direction[1]
        elif direction[0] == "up":
            aim -= direction[1]
        elif direction[0] == "down":
            aim += direction[1]

    print(f"aim:{aim}, forward:{forward} * depth:{depth} = {forward*depth}")

def main():
    parser = argparse.ArgumentParser(description="Compute path.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                compute_path(input_file)
            elif args.part == 2:
                compute_path_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


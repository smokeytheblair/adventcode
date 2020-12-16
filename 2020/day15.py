import sys
import argparse
from collections import defaultdict

reset_report = None

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def load_inputs(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        for line in input_file:
            report.append(line[:-1]) #remove \n

        if reset_report is None:
            reset_report = report.copy()

    return report

def convert_program(program):
    return [int(x) for x in program[0].split(",")]

def run_program(program, n):
    print(f"run_program: {program}")

    index = len(program)
    num = program[-1:][0]
    next_num = 0
    game = program[:-1]
    
    while index < n:
#        print(f"num: {num}, index: {index}, game: {game}")
        if num in game:
            next_num = (index - 1) - (len(game) - game[::-1].index(num) - 1)
        else:
            next_num = 0

#        print(f"num: {num}, next_num: {next_num}")
        game.append(num)
        num = next_num
        index += 1

            
#        print(num)
    
    return num

def part_1(input_file, n):
    program = load_inputs(input_file)
    print(program)
    program = convert_program(program)

    number = run_program(program, n)

    print(f"{number}")

def part_2(input_file, n):
    program = load_inputs(input_file)
    print(program)
    program = convert_program(program)

    number = run_program(program, n)

    print(f"{number}")

def main():
    parser = argparse.ArgumentParser(description="Load docking program.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                part_1(input_file, 2020)
            elif args.part == 2:
                part_2(input_file, 30000000)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()

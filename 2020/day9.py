import sys
import argparse
import math
import itertools

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

def make_XMAS_code(codes):
    new_code = []

    for num in codes:
        new_code.append(int(num))

    return new_code

def test_codes(codes, preamble):
    index = 0
    for index in range(len(codes)):
        if index < preamble:
            index += 1
            continue
        code_passes = False
        for num_a, num_b in itertools.combinations(codes[index-preamble:index], 2):
            if num_a + num_b == codes[index]:
                code_passes = True

        if code_passes == False:
            print(f"Failed code: {codes[index]}")


def part_1(input_file, preamble):
    codes = make_XMAS_code(load_inputs(input_file))
    test_codes(codes, preamble)    

def part_2(input_file):
    instructions = load_inputs(input_file)
    program = make_program(instructions)
    
    finish_normally = False
    for index in range(len(program)): 
        if fix_program(input_file, index):
            break
            

def main():
    parser = argparse.ArgumentParser(description="Find incorrect XMAS code.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')
    parser.add_argument('--preamble', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                part_1(input_file, int(args.preamble))
            elif args.part == 2:
                part_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


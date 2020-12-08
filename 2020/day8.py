import sys
import argparse
import math

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

def make_program(instructions):
    program = []

    for instruction in instructions:
        splits = instruction.split(" ")
        splits.append(0)
#        print(f"{splits}")
        program.append(splits)

    return program

def part_1(input_file):
    instructions = load_inputs(input_file)
    program = make_program(instructions)
    
    accumulator = 0
    instr = 0
    while instr < len(program):
        instruction = program[instr]
        if instruction[2] > 0 :
            break
        
        instruction[2] += 1 #count of visits to this instruction
        print(f"{instruction}")
        if instruction[0] == "nop":
            instr += 1
        elif instruction[0] == "acc":
            accumulator += int(instruction[1])            
            instr += 1
        elif instruction[0] == "jmp":
            instr += int(instruction[1])

    print(f"Accumulator: {accumulator}")

def part_2(input_file):
    pass

def main():
    parser = argparse.ArgumentParser(description="In flight boot code.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                part_1(input_file)
            elif args.part == 2:
                part_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


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

def run_program(program):
    finished_normally = True
    accumulator = 0
    instr = 0
    last_instr = 0
    while instr < len(program):
        instruction = program[instr]
        if instruction[2] > 0 :
            finished_normally = False
            break
        
        instruction[2] += 1 #count of visits to this instruction
#        print(f"Last instruction ptr {last_instr}, current {instruction}")
        if instruction[0] == "nop":
            instr += 1
        elif instruction[0] == "acc":
            accumulator += int(instruction[1])            
            instr += 1
        elif instruction[0] == "jmp":
            instr += int(instruction[1])

        last_instr = instr

    if finished_normally:
        print(f"Accumulator: {accumulator}")

    return finished_normally

def fix_program(input_file, instr_index):
    instructions = load_inputs(input_file)
    program = make_program(instructions)

    if program[instr_index][0] == "nop":
        program[instr_index][0] = "jmp"
    elif program[instr_index][0] == "jmp":
        program[instr_index][0] = "nop"

    return run_program(program)

def part_1(input_file):
    instructions = load_inputs(input_file)
    program = make_program(instructions)
    
    run_program(program)

def part_2(input_file):
    instructions = load_inputs(input_file)
    program = make_program(instructions)
    
    finish_normally = False
    for index in range(len(program)): 
        if fix_program(input_file, index):
            break
            

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


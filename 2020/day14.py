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
    new_program = [] 

    for instr in program:
        vals = instr.split(" = ")
        new_program.append((vals[0], int(vals[1]) if (vals[1]).isnumeric() else vals[1]))
    
    return new_program

def apply_bitmask(bitmask, value, register):
    length = len(bitmask)
    val_bits = format(value, f"0{length}b") 
    reg_bits = format(register, f"0{length}b")
    new_bits ="" 
#    print(f"bitmask: {bitmask}, value: {value} or {val_bits}, reg: {register} or {reg_bits}")
    for mask, new_bit, reg_bit in zip(bitmask, val_bits, reg_bits):
        if mask == "X":
            new_bits += new_bit# if new_bit == "1" else new_bit
        else:
            new_bits += mask

#    print(f"new binary: {new_bits}")
    return int(new_bits, 2)

def run_program(program):
    registers = defaultdict(int)

    mask = ""
    for instr in program:
        key = instr[0]
        val = instr[1]

        if key == "mask":
            mask = val
        elif key.find("mem") != -1:
            register_num = int(key[4:-1])
            num = val
            new_num = apply_bitmask(mask, num, registers[register_num])
            registers[register_num] = new_num
#            print(f"num: {num}, new_num: {new_num}")
            
    return sum(registers.values())


def part_1(input_file):
    program = load_inputs(input_file)
    print(program)
    program = convert_program(program)

    number = run_program(program)

    print(f"{number}")

def part_2(input_file):
    pass

def main():
    parser = argparse.ArgumentParser(description="Load docking program.")
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

#!/usr/bin/env python3

import sys
import math
import argparse

reset_program = None

def print_usage(name):
    print("python3 {} <input file>".format(name))

def get_param_modes(command_in):
    command = command_in.zfill(5)
    params_len = len(command)
    modes = []
    
    if params_len == 5:
        modes.append(int(command[0]))
    else:
        modes.append(0)

    if params_len >= 4:
        modes.append(int(command[1]))
    else:
        modes.append(0)

    if params_len >= 3:
        modes.append(int(command[2]))
    else:
        modes.append(0)

    # print(f'modes = {modes}')

    return modes

def store_param(values, instr_ptr, input_param):
    command = values[instr_ptr]
    modes = get_param_modes(command)
    store_idx = int(values[int(instr_ptr)+1])
    values[store_idx] = input_param

    # print(f'store_param --> {store_idx} = {input_param}')
    

def output_param(values, instr_ptr):
    command = values[instr_ptr]
    modes = get_param_modes(command)
    output_idx = 0
    if modes[2] == 0:
       output_idx = int(values[int(instr_ptr)+1])
       print(f'Output command = {values[output_idx]}')
    else:
       print(f'Output command = {values[int(instr_ptr+1)]}')

def do_add(values, instr_ptr):
    command = values[instr_ptr]
    modes = get_param_modes(command)

    op_1_idx = 0
    op_2_idx = 0
    result_idx = 0

    if modes[2] == 0:
        op_1_idx = int(values[instr_ptr+1])
    else:
        op_1_idx = instr_ptr+1

    if modes[1] == 0:
        op_2_idx = int(values[instr_ptr+2])
    else:
        op_2_idx = instr_ptr+2

    if modes[0] == 0:
        result_idx = int(values[instr_ptr+3])
    else:
        result_idx = instr_ptr+3

    values[result_idx] = str(int(values[op_1_idx]) + int(values[op_2_idx]))
    # print(f'do_add at {instr_ptr} => values[{result_idx}] = {values[result_idx]}')

def do_multiply(values, instr_ptr):
    command = values[instr_ptr]
    modes = get_param_modes(command)

    op_1_idx = 0
    op_2_idx = 0
    result_idx = 0

    if modes[2] == 0:
        op_1_idx = int(values[instr_ptr+1])
    else:
        op_1_idx = instr_ptr+1

    if modes[1] == 0:
        op_2_idx = int(values[instr_ptr+2])
    else:
        op_2_idx = instr_ptr+2

    if modes[0] == 0:
        result_idx = int(values[instr_ptr+3])
    else:
        result_idx = instr_ptr+3

    values[result_idx] = str(int(values[op_1_idx]) * int(values[op_2_idx]))
    # print(f'do_multiply at {instr_ptr} => values[{result_idx}] = {values[result_idx]}')

def load_program(input_file):
    global reset_program
    program = []
    if reset_program is not None:
        program = reset_program.copy()
    else:
        index = 0

        for line in input_file:
            values = line.split(',')
            for number in values:
                program.append(number)
                index += 1

        if reset_program is None:
            reset_program = program.copy()

    return program

def process_program(input_file, input_param):
    program = load_program(input_file)
    print(f'{program} = {len(program)}')

    instr_ptr = 0

    while  instr_ptr < len(program):
        value = program[instr_ptr]
        op_code = int(value[-1:])
        # print(f'instr_ptr = {instr_ptr}, value = {value}, op_code = {op_code}')

        if value == '99':
            break
        if op_code is 1:
            do_add(program, instr_ptr)
            instr_ptr += 4
        if op_code == 2:
            do_multiply(program, instr_ptr)
            instr_ptr += 4
        if op_code == 3:
            store_param(program, instr_ptr, input_param)
            instr_ptr += 2
        if op_code == 4:
            output_param(program, instr_ptr)
            instr_ptr += 2

    # print(f'{program} = {len(program)}')
    # print(f'program[0] = {program[0]}')
    return program[0]

def main():
    parser = argparse.ArgumentParser(description='Compute required fuel for modules, or modules+fuel')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--input', type=int, required=False, default=0, help='Compute fuel for modules plus the loaded fuel.')

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.input is 1:
                answer = process_program(input_file, int(args.input))
                print(f'Answer = {answer}')
            # else:
            #     noun, verb = find_inputs(input_file, args.input)
            #    answer = 100 * noun + verb
            #    print(f'noun = {noun}, verb = {verb}, answer = {answer}')
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

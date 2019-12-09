#!/usr/bin/env python3

import sys
import math
import argparse

reset_program = None

def print_usage(name):
    print("python3 {} <input file>".format(name))

def get_param_modes(command_in, values, instr_ptr):
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

    result = (op_1_idx, op_2_idx, result_idx)
    # print(f'Indexes {result}')

    return result

def jump_if_true(values, instr_ptr):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr)

    if 0 != int(values[op_1_idx]):
        instr_ptr = int(values[op_2_idx])
    else:
        instr_ptr += 3

    return instr_ptr

def jump_if_false(values, instr_ptr):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr)

    if 0 == int(values[op_1_idx]):
        instr_ptr = int(values[op_2_idx])
    else:
        instr_ptr += 3

    return instr_ptr

def check_less_than(values, instr_ptr):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr)

    if int(values[op_1_idx]) < int(values[op_2_idx]):
        values[result_idx] = '1'
    else:
        values[result_idx] = '0'

def check_equals(values, instr_ptr):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr)

    if int(values[op_1_idx]) ==  int(values[op_2_idx]):
        values[result_idx] = '1'
    else:
        values[result_idx] = '0'

def store_param(values, instr_ptr, input_param):
    store_idx = int(values[int(instr_ptr)+1])
    values[store_idx] = input_param

    # print(f'store_param --> {store_idx} = {input_param}')
    

def output_param(values, instr_ptr):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr)
    print(f'Output command = {values[op_1_idx]}')

def do_add(values, instr_ptr):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr)

    values[result_idx] = str(int(values[op_1_idx]) + int(values[op_2_idx]))
    # print(f'do_add at {instr_ptr} => values[{result_idx}] = {values[result_idx]}')

def do_multiply(values, instr_ptr):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr)

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
        if op_code == 5:
            instr_ptr = jump_if_true(program, instr_ptr)
        if op_code == 6:
            instr_ptr = jump_if_false(program, instr_ptr)
        if op_code == 7:
            check_less_than(program, instr_ptr)
            instr_ptr += 4
        if op_code == 8:
            check_equals(program, instr_ptr)
            instr_ptr += 4

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
            if args.input is not 0:
                answer = process_program(input_file, int(args.input))
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

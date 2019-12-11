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
    # print(f'Output command = {values[op_1_idx]}')
    return values[op_1_idx]

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

def process_program(input_file, phase, prior_output):
    program = load_program(input_file)
    # print(f'{program} = {len(program)}')

    output = 0
    instr_ptr = 0
    first_input = True

    while  instr_ptr < len(program):
        value = program[instr_ptr]
        op_code = int(value[-1:])
        # print(f'instr_ptr = {instr_ptr}, value = {value}, op_code = {op_code}')

        if value == '99':
            break
        if op_code is 1: #add
            do_add(program, instr_ptr)
            instr_ptr += 4
        if op_code == 2: #multiply
            do_multiply(program, instr_ptr)
            instr_ptr += 4
        if op_code == 3: #store input
            if first_input is True:
                first_input = False
                store_param(program, instr_ptr, phase)
            else:
                store_param(program, instr_ptr, str(prior_output))
            instr_ptr += 2
        if op_code == 4: #output
            output = output_param(program, instr_ptr)
            instr_ptr += 2
        if op_code == 5: #jump true
            instr_ptr = jump_if_true(program, instr_ptr)
        if op_code == 6: #jump false
            instr_ptr = jump_if_false(program, instr_ptr)
        if op_code == 7: #le
            check_less_than(program, instr_ptr)
            instr_ptr += 4
        if op_code == 8: #eq
            check_equals(program, instr_ptr)
            instr_ptr += 4

#    print(f'program = {program}')

    return int(output)

def process_programs(input_file, phases):
    final_output = 0
    for test in phases:
        output = 0
        test_phases = test[:-1]

        #process each amp with new phase setting and with output of prior amp
        for phase in test_phases.split(','):
            output = process_program(input_file, phase, output)
            # print(f'phase:{phase} => {output}')
            
        final_output = max(final_output, output)
        print(f'Test[{test_phases}]******************{output}')

    print(f'Max output = {final_output}')
    
def main():
    parser = argparse.ArgumentParser(description='Compute required fuel for modules, or modules+fuel')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('phases', type=argparse.FileType('r'))

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            with args.phases as phases:
                answer = process_programs(input_file, phases)
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

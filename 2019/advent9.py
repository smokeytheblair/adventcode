#!/usr/bin/env python3

import sys
import math
import argparse
import numpy as np

reset_program = None

def print_usage(name):
    print("python3 {} <input file>".format(name))

def get_param_modes(command_in, values, instr_ptr, relative_base):
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
    elif modes[2] == 1:
        op_1_idx = instr_ptr+1
    else:
        op_1_idx = int(values[instr_ptr+1])+int(relative_base)

    if modes[1] == 0:
        op_2_idx = int(values[instr_ptr+2])
    elif modes[1] == 1:
        op_2_idx = instr_ptr+2
    else:
        op_2_idx = int(values[instr_ptr+2])+int(relative_base)

    if modes[0] == 0:
        if instr_ptr+3 < len(values):
            result_idx = int(values[instr_ptr+3])
        else:
            results_idx = 0
    elif modes[0] == 1:
        result_idx = instr_ptr+3
    else:
        if instr_ptr+3 < len(values):
            result_idx = int(values[instr_ptr+3])+int(relative_base)
        else:
            results_idx = 0

    result = (op_1_idx, op_2_idx, result_idx)
    # print(f'Indexes {result}')

    return result

def jump_if_true(values, extra_memory, instr_ptr, relative_base):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr, relative_base)

    if op_1_idx < len(values):
        if 0 != int(values[op_1_idx]):
            instr_ptr = int(values[op_2_idx]) if op_2_idx < len(values) else int(extra_memory[op_2_idx-len(values)])
        else:
            instr_ptr += 3
    else:
        if 0 != int(extra_memory[op_1_idx-len(values)]):
            instr_ptr = int(values[op_2_idx]) if op_2_idx < len(values) else int(extra_memory[op_2_idx-len(values)])
        else:
            instr_ptr += 3

    return instr_ptr

def jump_if_false(values, extra_memory, instr_ptr, relative_base):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr, relative_base)

    if op_1_idx < len(values):
        if 0 == int(values[op_1_idx]):
            instr_ptr = int(values[op_2_idx]) if op_2_idx < len(values) else int(extra_memory[op_2_idx-len(values)])
        else:
            instr_ptr += 3
    else:
        if 0 == int(extra_memory[op_1_idx-len(values)]):
            instr_ptr = int(values[op_2_idx]) if op_2_idx < len(values) else int(extra_memory[op_2_idx-len(values)])
        else:
            instr_ptr += 3

    return instr_ptr

def check_less_than(values, extra_memory, instr_ptr, relative_base):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr, relative_base)

    val1 = int(values[op_1_idx]) if op_1_idx < len(values) else int(extra_memory[op_1_idx-len(values)])
    val2 = int(values[op_2_idx]) if op_2_idx < len(values) else int(extra_memory[op_2_idx-len(values)])
    if result_idx < len(values):
        values[result_idx] = '1' if val1 < val2 else '0'
    else:
        extra_memory[result_idx-len(values)] = '1' if val1 < val2 else '0'

def check_equals(values, extra_memory, instr_ptr, relative_base):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr, relative_base)

    val1 = int(values[op_1_idx]) if op_1_idx < len(values) else int(extra_memory[op_1_idx-len(values)])
    val2 = int(values[op_2_idx]) if op_2_idx < len(values) else int(extra_memory[op_2_idx-len(values)])
    if result_idx < len(values):
        values[result_idx] = '1' if val1 == val2 else '0'
    else:
        extra_memory[result_idx-len(values)] = '1' if val1 == val2 else '0'

def store_param(values, extra_memory, instr_ptr, input_param, relative_base):
    op_code = values[instr_ptr]
    store_idx, op_2_idx, result_idx = get_param_modes(op_code, values, instr_ptr, relative_base)

    if store_idx < len(values):
        values[store_idx] = input_param
    else:
        extra_memory[store_idx-len(values)] = input_param
    # print(f'store_param --> {store_idx} = {input_param}')
    # print(f'program state = {values}')

def output_param(values, extra_memory, instr_ptr, relative_base):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr, relative_base)
    # print(f'Output command = {values[op_1_idx]}')
    output = 0
    if op_1_idx < len(values):
        output = values[op_1_idx]
    else:
        output = extra_memory[op_1_idx-len(values)]

    return output

def do_add(values, extra_memory, instr_ptr, relative_base):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr, relative_base)
    # print(f'op_1_idx, op_2_idx, result_idx = {op_1_idx}, {op_2_idx}, {result_idx}')
    # print(f'do_add at {instr_ptr} => values[{result_idx}] = {values[result_idx]}')

    val1 = int(values[op_1_idx]) if op_1_idx < len(values) else int(extra_memory[op_1_idx-len(values)])
    val2 = int(values[op_2_idx]) if op_2_idx < len(values) else int(extra_memory[op_2_idx-len(values)])

    if result_idx < len(values):
        values[result_idx] = str(val1 + val2)
    else:
        extra_memory[result_idx-len(values)] = str(val1 + val2)

def do_multiply(values, extra_memory, instr_ptr, relative_base):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr, relative_base)

    val1 = int(values[op_1_idx]) if op_1_idx < len(values) else int(extra_memory[op_1_idx-len(values)])
    val2 = int(values[op_2_idx]) if op_2_idx < len(values) else int(extra_memory[op_2_idx-len(values)])

    if result_idx < len(values):
        values[result_idx] = str(val1 * val2)
    else:
        extra_memory[result_idx-len(values)] = str(val1 * val2)
    # print(f'do_multiply at {instr_ptr} => values[{result_idx}] = {values[result_idx]}')

def update_relative_base(values, extra_memory, instr_ptr, relative_base):
    command = values[instr_ptr]
    op_1_idx, op_2_idx, result_idx = get_param_modes(command, values, instr_ptr, relative_base)

    relative_delta = 0
    if op_1_idx < len(values):
        relative_delta = int(values[op_1_idx])
    else:
        relative_delta = int(extra_memory[op_1_idx-len(values)])

    return int(relative_base + relative_delta)
    
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
                program.append(number.strip())
                index += 1

        if reset_program is None:
            reset_program = program.copy()

    extra_memory = np.full(256, 0)
    # print(f'{program} = {len(program)}')
    return (program, extra_memory)

def process_program(program, extra_memory, input_param):
    relative_base = 0
    output = 0
    instr_ptr = 0

    while  instr_ptr < len(program):
        value = program[instr_ptr]
        op_code = int(value[-1:])
        # print(f'instr_ptr = {instr_ptr}, value = {value}, op_code = {op_code}')

        if value == '99':
            break
        if op_code is 1: #add
            # print(f'do_add(program, {instr_ptr}, {relative_base})')
            do_add(program, extra_memory, instr_ptr, relative_base)
            instr_ptr += 4
        if op_code == 2: #multiply
            do_multiply(program, extra_memory, instr_ptr, relative_base)
            instr_ptr += 4
        if op_code == 3: #store input
            # print(f'amp {amp_index} storing input from amp {(amp_index-1)%5}')
            prior_output = input_param
            store_param(program, extra_memory, instr_ptr, str(prior_output), relative_base)
            instr_ptr += 2
        if op_code == 4: #output
            output = output_param(program, extra_memory, instr_ptr, relative_base)
            print(f'output --> {output}')
            instr_ptr += 2
        if op_code == 5: #jump true
            instr_ptr = jump_if_true(program, extra_memory, instr_ptr, relative_base)
        if op_code == 6: #jump false
            instr_ptr = jump_if_false(program, extra_memory, instr_ptr, relative_base)
        if op_code == 7: #le
            check_less_than(program, extra_memory, instr_ptr, relative_base)
            instr_ptr += 4
        if op_code == 8: #eq
            check_equals(program, extra_memory, instr_ptr, relative_base)
            instr_ptr += 4
        if op_code == 9: #update relative_base
            relative_base = update_relative_base(program, extra_memory, instr_ptr, relative_base)
            instr_ptr += 2

    # print(f'program = {program}')

    return int(output)

def process_programs(input_file, input_param):
    final_output = {} 

    program, extra_memory = load_program(input_file)
    print(f'program length = {len(program)}')

    result = process_program(program, extra_memory, input_param)

    print(f'Max output {result}')
    return result
    
def main():
    parser = argparse.ArgumentParser(description='Compute required fuel for modules, or modules+fuel')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--input-param', type=int, required=True)

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            answer = process_programs(input_file, args.input_param)
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

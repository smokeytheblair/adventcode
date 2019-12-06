#!/usr/bin/env python3

import sys
import math
import argparse

reset_program = None

def print_usage(name):
    print("python3 {} <input file>".format(name))

def do_add(values, instr_ptr):
    op_1_idx = values[instr_ptr+1]
    op_2_idx = values[instr_ptr+2]
    result_idx = values[instr_ptr+3]
    values[result_idx] = values[op_1_idx] + values[op_2_idx]    
    print(f'do_add at {instr_ptr} => values[{result_idx}] = {values[result_idx]}')

def do_multiply(values, instr_ptr):
    op_1_idx = values[instr_ptr+1]
    op_2_idx = values[instr_ptr+2]
    result_idx = values[instr_ptr+3]
    values[result_idx] = values[op_1_idx] * values[op_2_idx]    
    print(f'do_multiply at {instr_ptr} => values[{result_idx}] = {values[result_idx]}')

def load_program(input_file, noun, verb):
    global reset_program
    program = []
    if reset_program is not None:
        program = reset_program.copy()
        program[1] = noun
        program[2] = verb
    else:
        index = 0

        for line in input_file:
            values = line.split(',')
            for number in values:
                program.append(int(number))
                index += 1

        if reset_program is None:
            reset_program = program.copy()

        # repair the program
        program[1] = noun 
        program[2] = verb

    return program

def process_program(input_file, noun, verb):
    program = load_program(input_file, noun, verb)
    print(f'{program} = {len(program)}')

    for instr_ptr in range(0, len(program), 4):
        value = program[instr_ptr]
        if value == 99:
            break
        if value is 1:
            do_add(program, instr_ptr)
        if value == 2:
            do_multiply(program, instr_ptr)

    print(f'{program} = {len(program)}')
    print(f'program[0] = {program[0]}')
    return program[0]

def find_inputs(input_file, find_code):
    for noun in range(0,100):
        for verb in range(0,100):
            answer = process_program(input_file, noun, verb)
            if (answer == find_code):
                return (noun, verb)

    return

def main():
    parser = argparse.ArgumentParser(description='Compute required fuel for modules, or modules+fuel')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--find-code', type=int, required=False, default=0, help='Compute fuel for modules plus the loaded fuel.')

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.find_code is 0:
                answer = process_program(input_file, 12, 2)
                print(f'Answer = {answer}')
            else:
                noun, verb = find_inputs(input_file, args.find_code)
                answer = 100 * noun + verb
                print(f'noun = {noun}, verb = {verb}, answer = {answer}')
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

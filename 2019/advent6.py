#!/usr/bin/env python3

import sys
import math
import argparse

def load_program(orbit_map):
    pass

def process_program(orbit_map):
    orbits = load_program(orbit_map)
    print(f'{orbits}')
    orbit_count = 0

    return orbit_count

def find_inputs(input_file, find_code):
    for noun in range(0,100):
        for verb in range(0,100):
            answer = process_program(input_file, noun, verb)
            if (answer == find_code):
                return (noun, verb)

    return

def main():
    parser = argparse.ArgumentParser(description='Compute direct + indirect orbits in the orbit map.')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--find-code', type=int, required=False, default=0, help='Compute fuel for modules plus the loaded fuel.')

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.find_code is 0:
                answer = process_program(input_file)
                print(f'Answer = {answer}')
            else:
                noun, verb = find_inputs(input_file, args.find_code)
                answer = 100 * noun + verb
                print(f'noun = {noun}, verb = {verb}, answer = {answer}')
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

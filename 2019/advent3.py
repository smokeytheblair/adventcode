#!/usr/bin/env python3

import sys
import math
import argparse

def main():
    parser = argparse.ArgumentParser(description='Find the clossing wire crossing to the center point.')
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

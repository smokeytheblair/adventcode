#!/usr/bin/env python3

import sys
import math
import argparse

def compute_how_many_passwords(input_file):
    pass

def main():
    parser = argparse.ArgumentParser(description='How many passwords?')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--shortest-path', action='store_true', default=False, help='part 2 of the day.')

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.shortest_path is False:
                compute_how_many_passwords(input_file)
            else:
                find_shortest_path(input_file)
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

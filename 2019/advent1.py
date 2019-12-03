#!/usr/bin/env python3

import sys
import math
import argparse

def print_usage(name):
    print("python3 {} <input file>".format(name))

def compute_module_fuel(mass):
    fuel = math.floor(mass/3) - 2;
    if fuel < 0:
        fuel = 0

    return fuel

def compute_module_and_fuel(mass):
    fuel = compute_module_fuel(mass)

    additional_fuel = compute_module_fuel(fuel)

    while additional_fuel > 0:
        print(f'additional_fuel is {additional_fuel}')
        fuel += additional_fuel
        additional_fuel = compute_module_fuel(additional_fuel)

    return fuel

def compute_total_fuel(input_file,name, modules_and_fuel):
    total_fuel = 0
    for module in input_file:
        if modules_and_fuel is True:
            total_fuel += compute_module_and_fuel(int(module))
        else:
            total_fuel += compute_module_fuel(int(module))

    return total_fuel

def main():
    parser = argparse.ArgumentParser(description='Compute required fuel for modules, or modules+fuel')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--modules-and-fuel', action='store_true', default=False, help='Compute fuel for modules plus the loaded fuel.')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            total_fuel = compute_total_fuel(input_file,sys.argv[1], args.modules_and_fuel)
            print(f'Total fuel required = {total_fuel}')
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

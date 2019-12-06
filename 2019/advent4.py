#!/usr/bin/env python3

import sys
import math
import argparse

def has_double_digits(passcode, only_pair):
    if only_pair is False:
        for idx in range(len(passcode)-1):
            if passcode[idx] == passcode[idx+1]:
                return True

        return False
    else:
        last_digit = passcode[0]
        count =1 
        for idx in range(1, len(passcode)):
            if last_digit == passcode[idx]:
                count += 1
            elif count == 2:
                return True
            else:
                count = 1
                last_digit = passcode[idx]

        if count == 2:
            return True
        else:
            return False

def digits_increase(passcode):
    for idx in range(len(passcode)-1):
        if int(passcode[idx]) > int(passcode[idx+1]):
            return False

    return True

def has_six_digits(passcode):
    return len(passcode) == 6

def compute_how_many_passwords(input_file, only_pair):
    low_num = 0
    high_num = 0
    numbers = []
    count = 0
    
    for line in input_file:
       numbers = line.split('-') 

    low_num = int(numbers[0])
    high_num = int(numbers[1])

    for number in range(low_num, high_num+1):
        if has_six_digits(str(number)) and has_double_digits(str(number), only_pair) and digits_increase(str(number)):
            count += 1

    print(f'Count of possible passcodes = {count}')

def main():
    parser = argparse.ArgumentParser(description='How many passwords?')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--only-pair', action='store_true', default=False, help='part 2 of the day.')

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            compute_how_many_passwords(input_file, args.only_pair)
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

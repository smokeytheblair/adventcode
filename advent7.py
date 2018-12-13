import sys
import re


def print_usage(name):
    print("python3 {} <input_file>".format(name))
    print("-1 - compute the first part of the problem.")
    print("-2 - compute the second part of the problem.")

def process_prereqs(input_file):
    print("processing prerequisite sequence...")

def main():
    if len(sys.argv) > 2:
        input_file = open(sys.argv[2], 'r')
        if "-1" in sys.argv[1]:
            process_prereqs(input_file)
        elif: "-2" in sys.argv[2]:
            process_part2(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

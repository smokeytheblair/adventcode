import sys
from datetime import datetime
import re


def print_usage(name):
    print("python3 {} <input_file>".format(name))


def main():
    if len(sys.argv) > 1:
        input_file = open(sys.argv[1], 'r')
        # find_tired_guard(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

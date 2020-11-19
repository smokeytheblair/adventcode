import sys
import math
import argparse

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def main():
    parser = argparse.ArgumentParser(description='Compute required fuel for modules, or modules+fuel')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--modules-and-fuel', action='store_true', default=False, help='Compute fuel for modules plus the loaded fuel.')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        pass
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


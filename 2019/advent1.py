import sys
import math

def print_usage(name):
    print("python3 {} <input file>".format(name))

def compute_module_fuel(mass):
    fuel = math.floor(int(mass)/3) - 2;
    return fuel

def compute_total_fuel(input_file,name):
    total_fuel = 0
    for module in input_file:
        total_fuel += compute_module_fuel(module)

    return total_fuel

def main():
    if (len(sys.argv) > 1):
        input_file = open(sys.argv[1], 'r')
        print(compute_total_fuel(input_file,sys.argv[1]))
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

import sys
import argparse

reset_report = None

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def load_inputs(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        report = list(input_file)

        if reset_report is None:
            reset_report = report.copy()

    inputs = []
    for line in report:
        inputs.append(line)

    return inputs

def compute_power(input_file):
    directions = load_inputs(input_file)
    print(f"{directions}")

    num_bits = len(directions[0])-1
    count_0 = 0
    count_1 = 0
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(num_bits):
        count_0 = 0
        count_1 = 0
        print(f"i: {i}")
        for direction in directions:
            print(f"direction[{i}] = {direction[i]}")
            if direction[i] == "0":
                count_0 += 1
            else:
                count_1 += 1

        print(f"count_0:{count_0}, count_1:{count_1}")

        if count_0 > count_1:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"


    gamma_int = int(gamma_rate, 2)
    epsilon_int = int(epsilon_rate, 2)

    print(f"gamma rate:{gamma_int} * epsilon rate:{epsilon_int} = {gamma_int*epsilon_int}")

    
def compute_power_2(input_file):
    directions = load_inputs(input_file)

    aim = 0
    forward = 0
    depth = 0
    for direction in directions:
        if direction[0] == "forward":
            forward += direction[1]
            depth += aim * direction[1]
        elif direction[0] == "up":
            aim -= direction[1]
        elif direction[0] == "down":
            aim += direction[1]

    print(f"aim:{aim}, forward:{forward} * depth:{depth} = {forward*depth}")

def main():
    parser = argparse.ArgumentParser(description="Compute power.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                compute_power(input_file)
            elif args.part == 2:
                compute_power_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


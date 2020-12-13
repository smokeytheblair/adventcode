import sys
import argparse
import math
import itertools

reset_report = None

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def load_inputs(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        for line in input_file:
            report.append(line[:-1]) #remove \n

        if reset_report is None:
            reset_report = report.copy()

    return report

def convert_routes(bus_routes):
    arrival = int(bus_routes[0])
    buses = bus_routes[1].replace("x,", "").split(",")
    buses = [int(bus) for bus in buses]
        
    return (arrival, buses)

def find_soonest_bus(arrival, buses):
    deltas = []

    for bus in buses:
        temp = arrival//int(bus)
        deltas.append(((temp + 1) * bus) - arrival)

    bus_id = buses[deltas.index(min(deltas))]
    delta = min(deltas)
    print(f"deltas: {deltas}")
    print(f"min deltas: {delta}")
    print(f"bus id: {bus_id}")
    return (bus_id, delta)

def part_1(input_file):
    bus_routes = load_inputs(input_file)
    arrival, buses = convert_routes(bus_routes)

    bus_id, delta = find_soonest_bus(arrival, buses)

    print(f"{bus_id} * {delta} = {bus_id * delta}")

def part_2(input_file):
    pass

def main():
    parser = argparse.ArgumentParser(description="Find bus routes.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                part_1(input_file)
            elif args.part == 2:
                part_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


import sys
import argparse
import math
from collections import defaultdict

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

def convert_routes_with_gaps(bus_routes):
    arrival = int(bus_routes[0])
    buses = bus_routes[1].split(",")

    for bus in buses:
        if bus.isnumeric():
            buses[buses.index(bus)] = int(bus)
    
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

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a * b //  gcd(a, b)

def find_soonest_series(buses):
    bus_index = []
    just_buses = []
    first_bus = None
    offset = 0
    for bus in buses:
        if type(bus) == int:
            bus_index.append(buses.index(bus))
            just_buses.append(bus)
            if first_bus is None:
                first_bus =  bus

    offset = first_bus
    t = first_bus * max(just_buses)
    print(f"starting the search at t: {t}")
    failed = False
    while not failed:
        for index in bus_index:
#            print (f"index: {index}, bus: {buses[index]}, t: {t}")
#            print(f"(t%bus) - index == {(t%buses[index])-index}")
            if 0 != ((t+index) % buses[index]):
                failed = True
                 
        if not failed:
            break;
        t += offset
        failed = False

    print(f"t: {t}")
    return t

def part_1(input_file):
    bus_routes = load_inputs(input_file)
    arrival, buses = convert_routes(bus_routes)

    bus_id, delta = find_soonest_bus(arrival, buses)

    print(f"{bus_id} * {delta} = {bus_id * delta}")

def part_2(input_file):
    bus_routes = load_inputs(input_file)
    arrival, buses = convert_routes_with_gaps(bus_routes)

    timestamp = find_soonest_series(buses)

    print(f"buses: {buses} line up at {timestamp}")

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

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

def process_navigation(direction, magnitude, curr_direction, x, y):
    new_x, new_y = x, y
    new_dir = curr_direction
    directions = ["N", "E", "S", "W"]

    if direction == "N":
        new_y -= magnitude
    if direction == "S":
        new_y += magnitude
    if direction == "E":
        new_x += magnitude
    if direction == "W":
        new_x -= magnitude
    if direction == "F":
        if curr_direction == "N":
            new_y -= magnitude
        if curr_direction == "S":
            new_y += magnitude
        if curr_direction == "E":
            new_x += magnitude
        if curr_direction == "W":
            new_x -= magnitude
    if direction == "R":
       turns = magnitude//90
       curr_index = directions.index(curr_direction)
       new_dir = directions[(curr_index+turns)%4]
    if direction == "L":
       turns = magnitude//90
       curr_index = directions.index(curr_direction)
       new_dir = directions[(curr_index-turns)%4]

    return (new_x, new_y, new_dir)

def part_1(input_file):
    navigation = load_inputs(input_file)
    
    curr_direction = "E"
    x, y = 0, 0
    for nav in navigation:
        direction = nav[0]
        magnitude = int(nav[1:])

        x, y, curr_direction = process_navigation(direction, magnitude, curr_direction, x, y)
        print(f"x: {x}, y: {y}, curr_direction: {curr_direction}")

    print(f"{x} + {y} == {x+y}")

def part_2(input_file):
    pass

def main():
    parser = argparse.ArgumentParser(description="Compute distance.")
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


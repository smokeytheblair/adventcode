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

def print_seating(seating):
    occupied_seats = 0
    for row in seating:
        occupied_seats += row.count("#") 
        print(row)

    print(f"Occupied seats: {occupied_seats}")

def should_sit(seating, row_index, col_index):
    new_seat = seating[row_index][col_index]
    new_seat = "#"
    return new_seat

def should_stand(seating, row_index, col_index):
    new_seat = seating[row_index][col_index]
    new_seat = "#"
    return new_seat

def find_seat_status(seating, row_index, col_index):
    current_seat = seating[row_index][col_index]
#    print(f"seat[{row_index}][{col_index}] = {current_seat}")

    if current_seat == "L":
        current_seat = should_sit(seating, row_index, col_index)
    elif current_seat == "#":
        current_seat = should_stand(seating, row_index, col_index)
    else: # "."
        pass

    return current_seat

def apply_rules(seating):
    new_seating = []
    new_row = ""

    for row_index in range(len(seating)):
        for col_index in range(len(seating[row_index])):
            seat_status = find_seat_status(seating, row_index, col_index)
            new_row += seat_status
        
        new_seating.append(new_row)
        new_row = ""

    return new_seating

def compare_seating_charts(old_seating, new_seating):
    return True

def part_1(input_file):
    seating = load_inputs(input_file)
    print_seating(seating)
    
    new_seating = apply_rules(seating)
    print_seating(new_seating)

    while not compare_seating_charts(seating, new_seating):
        print_seating(new_seating)
        seating = new_seating
        new_seating = apply_rules(seating)
        break

def part_2(input_file):
    print(f"part2")

def main():
    parser = argparse.ArgumentParser(description="Arrange seating.")
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


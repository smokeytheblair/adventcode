import sys
import argparse
import math

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
            report.append(line[:-1])

        if reset_report is None:
            reset_report = report.copy()

    return report

def find_row(boarding_pass, min_row, max_row):
########    print(f"find_row({boarding_pass}, {min_row}, {max_row})")
    row = (max_row + min_row) // 2

    if len(boarding_pass) == 0:
        return row
    
    letter = boarding_pass[0]

    if letter == "F":
        row = find_row(boarding_pass[1:], min_row, row)
    elif letter == "B":
        row = find_row(boarding_pass[1:], row+1, max_row)

    return row

def find_column(boarding_pass, min_col, max_col):
#    print(f"find_column({boarding_pass}, {min_col}, {max_col})")
    col = (max_col + min_col) // 2
    
    if len(boarding_pass) == 0:
        return col

    boarding_pass = boarding_pass.replace("F", "")
    boarding_pass = boarding_pass.replace("B", "")
    letter = boarding_pass[0]

    if letter == "L":
        col = find_column(boarding_pass[1:], min_col, col)
    elif letter == "R":
        col = find_column(boarding_pass[1:], col+1, max_col)
        
    return col

def seat_id(boarding_pass, min_row, max_row, min_col, max_col):
    current_seat_id = 0

    row = find_row(boarding_pass, min_row, max_row-1)
#    print(f"{boarding_pass} row {row}")
    col = find_column(boarding_pass, min_col, max_col-1)
#    print(f"{boarding_pass} col {col}")

    current_seat_id = (row * 8) + col

    return current_seat_id

def part_1(input_file, min_row, max_row, min_col, max_col):
    passes = load_inputs(input_file)
    
#    print(passes)
    highest_seat = 0

    for boardingpass in passes:
        current_seat_id = seat_id(boardingpass, min_row, max_row, min_col, max_col)
        print(f"{boardingpass} has seat id {current_seat_id}")
        if highest_seat < current_seat_id:
            highest_seat = current_seat_id

    print(f"Highest seat id: {highest_seat}")
    return highest_seat

def part_2(input_file, min_row, max_row, min_col, max_col):
    passes = load_inputs(input_file)
    
#    print(passes)
    my_seat = 0

    seats = []
    for boardingpass in passes:
        current_seat_id = seat_id(boardingpass, min_row, max_row, min_col, max_col)
#        print(f"{boardingpass} has seat id {current_seat_id}")
        if current_seat_id not in seats:
            seats.append(current_seat_id)

    last_seat = 0
    seats.sort()
    print(seats)
    for sid in seats:
        if last_seat == 0:
            last_seat = sid

        if sid != last_seat and abs(sid - last_seat) == 2:
            my_seat = last_seat + 1

        
    print(f"My seat id: {my_seat}")
    return my_seat


def main():
    parser = argparse.ArgumentParser(description="compute boarding passes.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                part_1(input_file, 0, 127, 0, 7)
            elif args.part == 2:
                part_2(input_file, 0, 127, 0, 7)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


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

def find_seat_left(seating, curr_row, curr_col):
    if curr_col <= 0:
        return None
    
    return seating[curr_row][curr_col-1]

def find_seat_right(seating, curr_row, curr_col):
    if curr_col >= len(seating[curr_row])-1:
        return None

    return seating[curr_row][curr_col+1]

def find_seat_down(seating, curr_row, curr_col):
    if curr_row >= len(seating)-1:
        return None

    return seating[curr_row+1][curr_col]

def find_seat_up(seating, curr_row, curr_col):
    if curr_row <= 0:
        return None

    return seating[curr_row-1][curr_col]

def find_seat_upleft(seating, curr_row, curr_col):
    if curr_row <= 0:
        return None
    if curr_col <= 0:
        return None

    return seating[curr_row-1][curr_col-1]

def find_seat_upright(seating, curr_row, curr_col):
    if curr_row <= 0:
        return None
    if curr_col >= len(seating[curr_row])-1:
        return None

    return seating[curr_row-1][curr_col+1]

def find_seat_downleft(seating, curr_row, curr_col):
    if curr_col <= 0:
        return None
    if curr_row >= len(seating) - 1:
        return None

    return seating[curr_row+1][curr_col-1]

def find_seat_downright(seating, curr_row, curr_col):
    if curr_row >= len(seating) - 1:
        return None
    if curr_col >= len(seating[curr_row])-1:
        return None

    return seating[curr_row+1][curr_col+1]

def should_sit(seating, row_index, col_index, first_seat):
    new_seat = seating[row_index][col_index]
    left, right, down, up = False, False, False, False
    upleft, upright, downleft, downright = False, False, False, False

    row_offset, col_offset = 0, 0

    # down
    if first_seat:
        while find_seat_down(seating, row_index+row_offset, col_index) == ".":
            row_offset += 1

    if find_seat_down(seating, row_index+row_offset, col_index) != "#":
        down = True

    row_offset = 0

    # up
    if first_seat:
        while find_seat_up(seating, row_index-row_offset, col_index) == ".":
            row_offset += 1

    if find_seat_up(seating, row_index-row_offset, col_index) != "#":
        up = True

    row_offset = 0

    # left
    if first_seat:
        while find_seat_left(seating, row_index, col_index-col_offset) == ".":
            col_offset += 1

    if find_seat_left(seating, row_index, col_index-col_offset) != "#":
        left = True

    col_offset = 0

    # right
    if first_seat:
        while find_seat_right(seating, row_index, col_index+col_offset) == ".":
            col_offset += 1

    if find_seat_right(seating, row_index, col_index+col_offset) != "#":
        right = True

    col_offset = 0

    # up-right
    if first_seat:
        while find_seat_upright(seating, row_index-row_offset, col_index+col_offset) == ".":
            col_offset += 1
            row_offset += 1

    if find_seat_upright(seating, row_index-row_offset, col_index+col_offset) != "#":
        upright = True

    row_offset, col_offset = 0, 0

    # down right
    if first_seat:
        while find_seat_downright(seating, row_index+row_offset, col_index+col_offset) == ".":
            col_offset += 1
            row_offset += 1

    if find_seat_downright(seating, row_index+row_offset, col_index+col_offset) != "#":
        downright = True

    row_offset, col_offset = 0, 0

    # down left
    if first_seat:
        while find_seat_downleft(seating, row_index+row_offset, col_index-col_offset) == ".":
            col_offset += 1
            row_offset += 1

    if find_seat_downleft(seating, row_index+row_offset, col_index-col_offset) != "#":
        downleft = True

    row_offset, col_offset = 0, 0

    # up left
    if first_seat:
        while find_seat_upleft(seating, row_index-row_offset, col_index-col_offset) == ".":
            col_offset += 1
            row_offset += 1

    if find_seat_upleft(seating, row_index-row_offset, col_index-col_offset) != "#":
        upleft = True
 
    if down and up and left and right and downleft and downright and upleft and upright:
        new_seat = "#"

    return new_seat

def should_stand(seating, row_index, col_index, occupied_limit, first_seat):
    new_seat = seating[row_index][col_index]
    count_occupied = 0
#    print(f"checking {row_index}, {col_index}, {new_seat}")

    row_offset, col_offset = 0, 0

    # down
    if first_seat:
        while find_seat_down(seating, row_index+row_offset, col_index) == ".":
            row_offset += 1

    if find_seat_down(seating, row_index+row_offset, col_index) == "#":
        count_occupied += 1

    row_offset = 0

    # up
    if first_seat:
        while find_seat_up(seating, row_index-row_offset, col_index) == ".":
            row_offset += 1

    if find_seat_up(seating, row_index-row_offset, col_index) == "#":
        count_occupied += 1

    row_offset = 0

    # left
    if first_seat:
        while find_seat_left(seating, row_index, col_index-col_offset) == ".":
            col_offset += 1

    if find_seat_left(seating, row_index, col_index-col_offset) == "#":
        count_occupied += 1

    col_offset = 0

    # right
    if first_seat:
        while find_seat_right(seating, row_index, col_index+col_offset) == ".":
            col_offset += 1

    if find_seat_right(seating, row_index, col_index+col_offset) == "#":
        count_occupied += 1

    col_offset = 0

    # up-right
    if first_seat:
        while find_seat_upright(seating, row_index-row_offset, col_index+col_offset) == ".":
            col_offset += 1
            row_offset += 1

    if find_seat_upright(seating, row_index-row_offset, col_index+col_offset) == "#":
        count_occupied += 1

    row_offset, col_offset = 0, 0

    # down right
    if first_seat:
        while find_seat_downright(seating, row_index+row_offset, col_index+col_offset) == ".":
            col_offset += 1
            row_offset += 1

    if find_seat_downright(seating, row_index+row_offset, col_index+col_offset) == "#":
        count_occupied += 1

    row_offset, col_offset = 0, 0

    # down left
    if first_seat:
        while find_seat_downleft(seating, row_index+row_offset, col_index-col_offset) == ".":
            col_offset += 1
            row_offset += 1

    if find_seat_downleft(seating, row_index+row_offset, col_index-col_offset) == "#":
        count_occupied += 1

    row_offset, col_offset = 0, 0

    # up left
    if first_seat:
        while find_seat_upleft(seating, row_index-row_offset, col_index-col_offset) == ".":
            col_offset += 1
            row_offset += 1

    if find_seat_upleft(seating, row_index-row_offset, col_index-col_offset) == "#":
        count_occupied += 1
 
    if count_occupied >= occupied_limit:
#        print(f"seat[{row_index}][{col_index}] has {count_occupied} occupied adjacent.")
        new_seat = "L"

    return new_seat

def find_seat_status(seating, row_index, col_index, occupied_limit, first_seat):
    current_seat = seating[row_index][col_index]
#    print(f"seat[{row_index}][{col_index}] = {current_seat}")

    if current_seat == "L":
        current_seat = should_sit(seating, row_index, col_index, first_seat)
    elif current_seat == "#":
        current_seat = should_stand(seating, row_index, col_index, occupied_limit, first_seat)
    else: # "."
        pass

    return current_seat

def apply_rules(seating, occupied_limit, first_seat):
    new_seating = []
    new_row = ""

    for row_index in range(len(seating)):
        for col_index in range(len(seating[row_index])):
            seat_status = find_seat_status(seating, row_index, col_index, occupied_limit, first_seat)
            new_row += seat_status
        
        new_seating.append(new_row)
        new_row = ""

    return new_seating

def compare_seating_charts(old_seating, new_seating):
    index = 0
    for index in range(len(old_seating)):
        old_row = old_seating[index]
        new_row = new_seating[index]

        if old_row != new_row:
            return False

    return True

def part_1(input_file, occupied_limit):
    seating = load_inputs(input_file)
    print_seating(seating)
    
    new_seating = apply_rules(seating, occupied_limit, False)

    while compare_seating_charts(seating, new_seating) == False:
        print_seating(new_seating)
        seating = new_seating.copy()
        new_seating = apply_rules(seating, occupied_limit, False)

    print_seating(new_seating)

def part_2(input_file, occupied_limit):
    seating = load_inputs(input_file)
    print_seating(seating)
    
    new_seating = apply_rules(seating, occupied_limit, True)

    while compare_seating_charts(seating, new_seating) == False:
        print_seating(new_seating)
        seating = new_seating.copy()
        new_seating = apply_rules(seating, occupied_limit, True)

    print_seating(new_seating)

def main():
    parser = argparse.ArgumentParser(description="Arrange seating.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                part_1(input_file, 4)
            elif args.part == 2:
                part_2(input_file, 5)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


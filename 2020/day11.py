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
    left, right, down, up = False, False, False, False
    up_left, up_right, down_left, down_right = False, False, False, False

    # left
    if col_index == 0: 
        left = True
        up_left = True
        down_left = True
    elif seating[row_index][col_index-1] != "#":
        left = True

    # up left
    if col_index != 0:    
        # top edge - left
        if row_index == 0:
            up_left = True
        elif seating[row_index-1][col_index-1] != "#":
            up_left = True
    
        # bottom edge - left
        if row_index == len(seating)-1:
            down_left = True
        elif seating[row_index+1][col_index-1] != "#":
            down_left = True
        
    # right
    if col_index == len(seating[row_index])-1:
        right = True
        down_right = True
        up_right = True
    elif seating[row_index][col_index+1] != "#":
        right = True 

    if col_index < len(seating[row_index])-1:
        # top edge
        if row_index == 0:
            up_right = True
        elif seating[row_index-1][col_index+1] != "#":
            up_right = True
        # bottom edge
        if row_index == len(seating)-1:
            down_right = True
        elif seating[row_index+1][col_index+1] != "#":
            down_right = True

    # up
    if row_index == 0:
        up = True
        up_left = True
        up_right = True
    elif seating[row_index-1][col_index] != "#":
        up = True

    # down
    if row_index == len(seating)-1:
        down = True
        down_left = True
        dodwn_right = True
    elif seating[row_index+1][col_index] != "#":
        down = True

    if left and right and up and down and up_left and down_left and up_right and down_right:
        new_seat = "#"

    return new_seat

def should_stand(seating, row_index, col_index, occupied_limit):
    new_seat = seating[row_index][col_index]
    count_occupied = 0

    # left edge
    if col_index == 0:
        pass
    elif seating[row_index][col_index-1] == "#":
        count_occupied +=1

    if col_index != 0:    
        # top edge - left
        if row_index == 0:
            pass
        elif seating[row_index-1][col_index-1] == "#":
            count_occupied += 1
    
        # bottom edge - left
        if row_index == len(seating)-1:
            pass
        elif seating[row_index+1][col_index-1] == "#":
            count_occupied +=1
        
    # right edge
    if col_index == len(seating[row_index])-1:
        pass
    elif seating[row_index][col_index+1] == "#":
        count_occupied +=1

    if col_index < len(seating[row_index])-1:
        # top edge
        if row_index == 0:
            pass
        elif seating[row_index-1][col_index+1] == "#":
            count_occupied += 1
        # bottom edge
        if row_index == len(seating)-1:
            pass
        elif seating[row_index+1][col_index+1] == "#":
            count_occupied +=1

    # top edge
    if row_index == 0:
        pass
    elif seating[row_index-1][col_index] == "#":
        count_occupied +=1
#        # left edge
#        if col_index == 0:
#            pass
#        elif seating[row_index-1][col_index - 1] == "#":
#            count_occupied += 1
#
#        #right edge
#        if col_index == len(seating[row_index]) - 1:
#            pass
#        elif seating[row_index-1][col_index+1] == "#":
#            count_occupied += 1

    # bottom edge
    if row_index == len(seating)-1:
        pass
    elif seating[row_index+1][col_index] == "#":
        count_occupied +=1
#        # left edge
#        if col_index == 0:
#            pass
#        elif seating[row_index+1][col_index - 1] == "#":
#            count_occupied += 1
#
#        #right edge
#        if col_index == len(seating[row_index]) - 1:
#            pass
#        elif seating[row_index+1][col_index+1] == "#":
#            count_occupied += 1
 
    if count_occupied >= occupied_limit:
#        print(f"seat[{row_index}][{col_index}] has {count_occupied} occupied adjacent.")
        new_seat = "L"

    return new_seat

def find_seat_status(seating, row_index, col_index, occupied_limit):
    current_seat = seating[row_index][col_index]
#    print(f"seat[{row_index}][{col_index}] = {current_seat}")

    if current_seat == "L":
        current_seat = should_sit(seating, row_index, col_index)
    elif current_seat == "#":
        current_seat = should_stand(seating, row_index, col_index, occupied_limit)
    else: # "."
        pass

    return current_seat

def apply_rules(seating, occupied_limit):
    new_seating = []
    new_row = ""

    for row_index in range(len(seating)):
        for col_index in range(len(seating[row_index])):
            seat_status = find_seat_status(seating, row_index, col_index, occupied_limit)
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
            print(f"index: {index}, old_row: {old_row}")
            print(f"index: {index}, new_row: {new_row}")
            return False

    return True

def part_1(input_file, occupied_limit):
    seating = load_inputs(input_file)
    print_seating(seating)
    
    new_seating = apply_rules(seating, occupied_limit)

    while compare_seating_charts(seating, new_seating) == False:
        print_seating(new_seating)
        seating = new_seating.copy()
        new_seating = apply_rules(seating, occupied_limit)

    print_seating(new_seating)

def part_2(input_file, occupied_limit):
    print(f"part2")

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


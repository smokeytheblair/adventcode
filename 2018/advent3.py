import sys
import re

def print_usage(name):
    print("python3 {} <input file>".format(name))

def is_isolated(square, squares):
    print("storing square {}".format(square))
    # #1307 @ 466,467: 14x16

    numbers = re.findall("\d+", square)
    # print("Processing estimate #{}".format(numbers[0]))

    start_y = int(numbers[1])
    start_x = int(numbers[2])
    range_y = int(numbers[3])
    range_x = int(numbers[4])

    for x in range(range_x):
        for y in range(range_y):
            inch = "{}:{}".format(start_x + x, start_y + y)
            if squares[inch] > 1:
                return False

    print("Isolated square {}".format(numbers[0]))

    return True

def store_square(square, squares):
    print("storing square {}".format(square))
    # #1307 @ 466,467: 14x16

    numbers = re.findall("\d+", square)
    # print("Processing estimate #{}".format(numbers[0]))

    start_y = int(numbers[1])
    start_x = int(numbers[2])
    range_y = int(numbers[3])
    range_x = int(numbers[4])

    for x in range(range_x):
        for y in range(range_y):
            inch = "{}:{}".format(start_x + x, start_y + y)
            # print(inch)
            squares.setdefault(inch, 0)
            squares[inch] += 1

    

def find_matching_squares(input_file, input_file2):
    print("finding matching squares...")

    squares = {}
    for square in input_file:
        store_square(square, squares)

    for square in input_file2:
        if is_isolated(square, squares):
            print("Found isolated square")
            break


    inches_count = 0
    for inch in squares:
        if (squares[inch] > 1):
            inches_count += 1

    print("Counted {} inches in overlap.".format(inches_count))

def main():
    if (len(sys.argv) > 1):
        input_file = open(sys.argv[1], 'r')
        input_file2 = open(sys.argv[1], 'r')
        find_matching_squares(input_file, input_file2)
        input_file2.close()
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

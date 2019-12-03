import sys

def print_usage(name):
    print("python3 {} <input file>".format(name))

def is_two(box):
    print("counting twos...")

    letter_counts = {}

    for letter in box:
        # print(letter)
        letter_counts.setdefault(letter, 0)
        letter_counts[letter] += 1
        # print("{} has count {}".format(letter, letter_counts[letter]))
    
    for letter in box:
        if (letter_counts[letter] == 2):
            print("box {} has two letter {}".format(box, letter))
            return True
        
    return False


def is_three(box):
    print("counting threes")

    letter_counts = {}

    for letter in box:
        # print(letter)
        letter_counts.setdefault(letter, 0)
        letter_counts[letter] += 1
        # print("{} has count {}".format(letter, letter_counts[letter]))

    
    for letter in box:
        if (letter_counts[letter] == 3):
            print("box {} has three letter {}".format(box, letter))
            return True
        
    return False


def count_boxes(input_file):
    print("counting boxes...")

    twos_count = 0
    threes_count = 0 

    for box in input_file:
        if is_two(box):
            twos_count += 1
        if is_three(box):
            threes_count += 1

    print("Resulting checksum {} x {} = {}".format(twos_count, threes_count, twos_count*threes_count))

def is_match(box1, box2):
    one_diff = False
    # print("\nchecking {} and {}".format(box1, box2))

    for i in range(len(box1)):
        # print("checking {} and {}".format(box1[i], box2[i]))
        if (box1[i] != box2[i]):
            if (one_diff == False):
                print("Setting one_diff to True.")
                one_diff = True
            else:
                print("Not a match. Moving to next box.")
                return False

    if (one_diff == True):
        print("Found a match!")
        return True
    else:
        return False

def find_match(input_file,name):
    print("finding matching boxes")

    compares_count = 0
    for box1 in input_file:
        print(box1)

        input2 = open(sys.argv[1], 'r')

        for box2 in input2:
            compares_count += 1
            print("\nComparison #{}".format(compares_count))
            if (is_match(box1, box2)):
                print("Box {} matches box {}.".format(box1, box2))
                return

        input2.close()

    print("Did not find any matches.")
    return

def main():
    if (len(sys.argv) > 1):
        input_file = open(sys.argv[1], 'r')
        # count_boxes(input_file)
        find_match(input_file,sys.argv[1])
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

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



def main():
    if (len(sys.argv) > 1):
        input_file = open(sys.argv[1], 'r')
        count_boxes(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

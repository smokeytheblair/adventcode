import sys

def print_usage(name):
    print("python3 {} <input file>".format(name))

def find_matching_squares(input_file):
    print("finding matching squares...")

def main():
    if (len(sys.argv) > 1):
        input_file = open(sys.argv[1], 'r')
        find_matching_squares(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

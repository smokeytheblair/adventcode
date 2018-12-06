import sys

def process_areas(input_file):
    print("Processing areas...")


def main():
    if len(sys.argv) > 1:
        input_file = open(sys.argv[1], 'r')
        process_areas(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

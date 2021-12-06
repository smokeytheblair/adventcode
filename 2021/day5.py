import sys
import argparse



def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def load_inputs(input_file):
    lines = list(input_file)

    vectors = []
    for line in lines:
        line = line.replace("\n", "")
        coords = line.split(" -> ")
        start_coords = coords[0].split(",")
        end_coords = coords[1].split(",")
        vectors.append((start_coords, end_coords))

    return vectors

def plot_vectors():
    pass

def find_overlaps(input_file):
    vectors = load_inputs(input_file)

    print(vectors)

def main():
    parser = argparse.ArgumentParser(description="Vents")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                find_overlaps(input_file)
            elif args.part == 2:
                find_overlaps(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


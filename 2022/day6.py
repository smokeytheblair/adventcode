import sys
import argparse

reset_report = None


def load_inputs(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        report = list(input_file)

        if reset_report is None:
            reset_report = report.copy()

    return report


def find_marker(input_file):
    datastream = load_inputs(input_file)[0]

    marker = 0
    last_four = []
    for i in range(len(datastream)):
        if 4 == len(last_four):
            if len(last_four) == len(set(last_four)):
                marker = i
                break

            last_four.pop(0)

        last_four.append(datastream[i])


    print(f"Start of packet marker = {marker}")


def find_marker_2(input_file):
    datastream = load_inputs(input_file)[0]

    marker = 0
    last_fourteen = []
    for i in range(len(datastream)):
        if 14 == len(last_fourteen):
            if len(last_fourteen) == len(set(last_fourteen)):
                marker = i
                break

            last_fourteen.pop(0)

        last_fourteen.append(datastream[i])


    print(f"Start of packet marker = {marker}")


def main():
    parser = argparse.ArgumentParser(description="Day 6")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                find_marker(input_file)
            elif args.part == 2:
                find_marker_2(input_file)


if __name__ == "__main__":
    main()


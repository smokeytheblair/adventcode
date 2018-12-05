import sys
from datetime import datetime


def print_usage(name):
    print("python3 {} <input_file>".format(name))

def sort_notes(input_file, notes):
    # [1518-05-01 23:46] Guard #2503 begins shift
    for note in input_file:
        timestamp = datetime.strptime(note[1:17], "%Y-%m-%d %H:%M")
        msg = note[19:]

        notes[timestamp] = msg

    for times in sorted(notes):
        print("{} {}".format(times, notes[times]))


def find_tired_guard(input_file):
    print("finding tired guard...")

    notes = {}
    sort_notes(input_file, notes)


def main():
    if len(sys.argv) > 1:
        input_file = open(sys.argv[1], 'r')
        find_tired_guard(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

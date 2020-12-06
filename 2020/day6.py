import sys
import argparse
import math
from collections import defaultdict

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
            report.append(line[:-1])

        if reset_report is None:
            reset_report = report.copy()

    return report

def make_groups(questions):
    answers = []
    group = ""
    for question in questions:
        if question != "":
            group += question
        else:
            answers.append(group)
            group = ""

    answers.append(group)

    return answers

def count_group(question):
    unique = []

    for letter in question:
        if letter not in unique:
            unique.append(letter)

    return len(unique)

def count_group_strict(question):
    unique = []

    for letter in question:
        if letter not in unique:
            unique.append(letter)

    return len(unique)

def part_1(input_file):
    questions = load_inputs(input_file)
    questions = make_groups(questions)
    
#    print(questions)

    counts = []
    for question in questions:
        length = count_group(question)
        counts.append(int(length))
#        print(f"{question}:{length}")

    print(f"Answer: {sum(counts)}")

def part_2(input_file):
    questions = load_inputs(input_file)
    
#    print(questions)

    members_in_group = 0
    counts = defaultdict(int)
    final_counts = 0
    for question in questions:
        if question == "":
            for answer in counts.values():
                if answer == members_in_group:
                    final_counts += 1

            members_in_group = 0
            counts = defaultdict(int)
            continue

        members_in_group += 1
        for letter in question:
            counts[letter] += 1
#        print(f"{question}:{length}")

    
    for answer in counts.values():
        if answer == members_in_group:
            final_counts += 1

    print(f"Answer: {final_counts}")

def main():
    parser = argparse.ArgumentParser(description="compute qustions.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                part_1(input_file)
            elif args.part == 2:
                part_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


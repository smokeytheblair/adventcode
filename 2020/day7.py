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
            report.append(line[:-2]) #remove \n and .

        if reset_report is None:
            reset_report = report.copy()

    return report

def make_rule_tree(rules):
    rule_tree = dict()

    for rule in rules:
        splits = rule.split(" contain ")
#        print(f"{splits}")
        key = splits[0]
        if "," in splits[1]:
            value = splits[1].split(", ")
        else:
            value = [splits[1]]

        key = key.replace(" bags", "")
        key = key.replace(" bag", "")

        new_vals = []
        for val in value:
            val = val.replace(" bags", "")
            val = val.replace(" bag", "")
            new_vals.append(val)

        rule_tree[key] = new_vals

    return rule_tree

def find_gold_bag(rule_tree, current_rule):
    if rule_tree.get(current_rule) is None:
        return False

    for inner_rule in rule_tree[current_rule]:
        if "shiny gold" in inner_rule:
            return True

        if find_gold_bag(rule_tree, inner_rule[2:]):
            return True

    return False

def part_1(input_file):
    rules = load_inputs(input_file)
    rules = make_rule_tree(rules)
    
#    print(rules)

    count = 0
    for rule in rules.keys():
#        perint(rule)
#        for inner in rules[rule]:
#            print(f"\t- {inner}")

        if find_gold_bag(rules, rule):
            count += 1
            print(f"{rule} can hold shiny gold")

    print(f"Bags that can hold shiny gold: {count}")

def part_2(input_file):
    pass

def main():
    parser = argparse.ArgumentParser(description="Figure luggage rules.")
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


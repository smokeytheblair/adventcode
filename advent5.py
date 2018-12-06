import sys
from datetime import datetime
import re

pairs = ['aA', 'Aa', 'bB', 'Bb', 'cC', 'Cc', 'dD', 'Dd', 'eE', 'Ee', 'fF', 'Ff', 'gG', 'Gg', 
        'hH', 'Hh', 'iI', 'Ii', 'jJ', 'Jj', 'kK', 'Kk', 'lL', 'Ll', 'mM', 'Mm', 'nN', 'Nn', 
        'oO', 'Oo', 'pP', 'Pp', 'qQ', 'Qq', 'rR', 'Rr', 'sS', 'Ss', 'tT', 'Tt', 'uU', 'Uu', 
        'vV', 'Vv', 'wW', 'Ww', 'xX', 'Xx', 'yY', 'Yy', 'zZ', 'Zz']

polymers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z']

def print_usage(name):
    print("python3 {} <input_file>".format(name))

def check_pairs(fabric):
    for pair in pairs:
        fabric = fabric.replace(pair, "")
    return fabric

def collapse_fabric(fabric):
    # print("collapsing fabric...")

    pairs_count = len(fabric)
    fabric = check_pairs(fabric)
    new_pairs_count = len(fabric)

    # print("Initial pairs count = {}".format(pairs_count))

    iterations = 1
    while pairs_count != new_pairs_count:
        # print("Iteration: {} - ({} | {})".format(iterations, pairs_count, new_pairs_count))
        pairs_count = new_pairs_count
        fabric = check_pairs(fabric)
        new_pairs_count = len(fabric)
        iterations += 1

    print("Iteration: {} - ({} | {})".format(iterations, pairs_count, new_pairs_count))
    # print("Final fabric: \n{}".format(fabric))
    print("Final pairs count = {}".format(new_pairs_count))

    return fabric

def process_fabric(input_file):
    print("Processing fabric...")
    fabric = input_file.read()
    fabric = fabric.replace("\n", "")

    fabric = collapse_fabric(fabric)

    # most_key = find_most_common_polymer(fabric)

    counts = {}
    for polymer in polymers:
        temp_fabric = fabric.replace(polymer, "")
        temp_fabric = temp_fabric.replace(polymer.upper(), "")
        temp_fabric = collapse_fabric(temp_fabric)
        counts[polymer] = len(temp_fabric)
        
    lowest_count = min(counts.values())
    print("Lowest count {}".format(lowest_count))


def main():
    if len(sys.argv) > 1:
        input_file = open(sys.argv[1], 'r')
        process_fabric(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

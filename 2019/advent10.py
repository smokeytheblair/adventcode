#!/usr/bin/env python3

import sys
import math
import argparse
import numpy as np


def print_usage(name):
    print("python3 {} <input file>".format(name))


def load_map(input_file):
    map = []

    for line in input_file:
        map_row = []
        for index in range(len(line)-1):
            map_row.append(line[index])
        map.append(map_row)

    return map


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def reduce_ratio(rise, run):
    ratio = None
    if run == 0:
        if rise >= 0:
            ratio = (1, 0)
        else:
            ratio = (-1, 0)
    else:
        gcd_val = abs(gcd(rise, run))
        # print(f'gcd_val({rise}, {run}) = {gcd_val}')

        rise_val = int(rise / gcd_val)

        run_val = int(run/gcd_val)

        ratio = (rise_val, run_val)

    return ratio


def find_best_asteroid(input_file):
    map = load_map(input_file)
    line_of_site = []
    print(f'map = {map}')

    for row_index in range(len(map)):
        line_of_site_row = np.full(len(map[row_index]), 0)
        line_of_site.append(line_of_site_row)
        for col_index in range(len(map[row_index])):
            if map[row_index][col_index] == '#':
                rise_over_run = {}
                for y in range(len(map)):
                    for x in range(len(map[y])):
                        if x == col_index and y == row_index:
                            continue
                        if map[y][x] == '#':
                            rise = y - row_index
                            run = x - col_index 
                            ratio = reduce_ratio(rise, run)
                            rise_over_run[ratio] = 1


                # print(f'rise_over_run map = {rise_over_run}')
                line_of_site[row_index][col_index] = len(rise_over_run)

    print(f'los = {line_of_site}')

    highest = 0
    highest_coords = None
    for x in range(len(line_of_site)):
        for y in range(len(line_of_site[x])):
            if line_of_site[x][y] > highest:
                highest = line_of_site[x][y]
                highest_coords = (x, y)
    
    return (highest_coords, highest)

def how_many_asteroids(best_asteroid):
    pass

def main():
    parser = argparse.ArgumentParser(description='find the best astroid for spotting the most asteroids.')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--modules-and-fuel', action='store_true', default=False, help='Compute fuel for modules plus the loaded fuel.')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            best_asteroid = find_best_asteroid(input_file)
            print(f'Most Asteroids = {best_asteroid}')
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

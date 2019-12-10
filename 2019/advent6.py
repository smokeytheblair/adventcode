#!/usr/bin/env python3

import sys
import argparse
from collections import defaultdict

def find_path(graph, start, end, path=None):
    if path is None:
        path = []

    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def load_program(orbit_map):
    orbits = defaultdict(list)
    planets = set()

    for orbit in orbit_map:
        parent_node, child_node = orbit.split(')')
        planets.add(parent_node)
        planets.add(child_node[:-1])
        orbits[parent_node].append(child_node[:-1])

    # print(f'planets = {planets}')
    return (orbits, planets)

def process_program(orbit_map):
    orbits, planets = load_program(orbit_map)
#    for orbit in orbits:
#        print(f'{orbit}: {orbits[orbit]}')
    orbit_count = 0

    for planet1 in planets:
        for planet2 in planets:
            path = find_path(orbits, planet1, planet2, []) 
            if path is not None and 1 < len(path):
                orbit_count += 1
#                if len(path) > 0:
#                print(f'path({planet1}, {planet2}) --> {path}: orbit_count = {orbit_count}')

    print(f'orbit_count = {orbit_count}')

    return orbit_count

def main():
    parser = argparse.ArgumentParser(description='Compute direct + indirect orbits in the orbit map.')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--find-code', type=int, required=False, default=0, help='Compute fuel for modules plus the loaded fuel.')

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.find_code is 0:
                answer = process_program(input_file)
                print(f'Answer = {answer}')
            else:
                pass
#                noun, verb = find_inputs(input_file, args.find_code)
#                answer = 100 * noun + verb
#                print(f'noun = {noun}, verb = {verb}, answer = {answer}')
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

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

def find_cousin(graph, start, end, path=None):
    path1 = find_path(graph, 'COM', 'SAN', [])
    path2 = find_path(graph, 'COM', 'YOU', [])

    path3 = list(set(path1) - set(path2))
    path4 = list(set(path2) - set(path1))
    
#    print(f'SAN path {path1}\nYOU path {path2}')
#    print(f'SAN path {path3} {len(path3)}')
#    print(f'YOU path {path4} {len(path4)}')

    return len(path3) + len(path4) - 2

def load_program(orbit_map):
    orbits = defaultdict(list)
    planets = set()

    for orbit in orbit_map:
        parent_node, child_node = orbit.split(')')
        planets.add(parent_node)
        planets.add(child_node[:-1])
        orbits[parent_node].append(child_node[:-1])

    print(f'planets = {planets}')
    return (orbits, planets)

def process_program(orbit_map, santa):
    orbits, planets = load_program(orbit_map)
#    for orbit in orbits:
#        print(f'{orbit}: {orbits[orbit]}')
    orbit_count = 0

    if santa is False:
        for planet1 in planets:
            for planet2 in planets:
                path = find_path(orbits, planet1, planet2, []) 
                if path is not None and 1 < len(path):
                    orbit_count += 1
#                    if len(path) > 0:
#                    print(f'path({planet1}, {planet2}) --> {path}: orbit_count = {orbit_count}')
        print(f'orbit_count = {orbit_count}')
    else:
        hops_count = find_cousin(orbits, 'YOU', 'SAN', [])
        print(f'path to Santa = {hops_count} hops.')


    return orbit_count

def main():
    parser = argparse.ArgumentParser(description='Compute direct + indirect orbits in the orbit map.')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--santa', action='store_true', required=False, default=False, help='Find path through orbits from YOU to SANta')

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            answer = process_program(input_file, args.santa)
            print(f'Answer = {answer}')
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

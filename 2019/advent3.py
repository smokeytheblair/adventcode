#!/usr/bin/env python3

import sys
import math
import argparse

def load_wires(input_file):
    wires = []
    for wire in input_file:
        temp_wire = [(node[0], int(node[1:])) for node in wire.split(',')]
        wires.append(temp_wire)
    
    return wires

def find_closest_intersect(intersects):
    distances = [abs(coord[0]) + abs(coord[1]) for coord in intersects]
    return min(distances)

def find_intersects(coords):
    # not intersects of coords, but intersects of line segments
    return list(set(coords[0]) & set(coords[1]))

def convert_to_coords(wire):
    coords = []

    origin = (0,0)
    coords.append(origin)

    for node in wire:
        if node[0] == 'U':
            x = coords[-1][0]
            orig_y = coords[-1][1]
            y = orig_y + node[1]
            for dot in range(orig_y+1, y):
                coords.append((x,dot))
            coords.append((x, y))
        elif node[0] == 'D':
            x = coords[-1][0]
            orig_y = coords[-1][1]
            y = orig_y - node[1]
            for dot in range(orig_y-1, y, -1):
                coords.append((x,dot))
            coords.append((x, y))
        elif node[0] == 'L':
            orig_x = coords[-1][0]
            x = orig_x - node[1]
            y = coords[-1][1]
            for dot in range(orig_x-1, x, -1):
                coords.append((dot, y))
            coords.append((x, y))
        elif node[0] == 'R':
            orig_x = coords[-1][0]
            x = orig_x + node[1]
            y = coords[-1][1]
            for dot in range(orig_x+1, x):
                coords.append((dot, y))
            coords.append((x, y))
        else:
            raise Exception()

    return coords[1:]

def compute_path_coords(wires):
    nodes = []

    for wire in wires:
        nodes.append(convert_to_coords(wire))

    return nodes

def find_coord_closest_to_origin(input_file):
    wires = load_wires(input_file)
    # print(f'Wires = {wires}')
    coords = compute_path_coords(wires)
    # print(f'Coords = {coords}')
    intersects = find_intersects(coords)
    print(f'Intersects = {intersects}')
    coord = find_closest_intersect(intersects)
    print(f'Closest intersect = {coord}')

def find_shortest_path(input_file):
    wires = load_wires(input_file)
    # print(f'Wires = {wires}')
    coords = compute_path_coords(wires)
    # print(f'Coords = {coords}')
    intersects = find_intersects(coords)
    print(f'Intersects = {intersects}')
    distances = []
    for intersect in intersects:
        distances.append(2 + coords[0].index(intersect) + coords[1].index(intersect))

    print(f'Distances = {distances}')
    print(f'Min path to intersect = {min(distances)}')

def main():
    parser = argparse.ArgumentParser(description='Find the clossing wire closest to the center point.')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--shortest-path', action='store_true', default=False, help='part 2 of the day.')

    args = parser.parse_args()

    print(args)

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.shortest_path is False:
                find_coord_closest_to_origin(input_file)
            else:
                find_shortest_path(input_file)
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

import sys
from collections import defaultdict
import re
from scipy import spatial

def print_usage(name):
    print("python3 {} <input_file>".format(name))


def load_coords(input_file):
    print("Loading coordinates...")

    coordinates = {}
    index = 0
    for coord in input_file:
        coordinates[index] = [int(x) for x in re.findall("\d+", coord)]
        index += 1

    print(coordinates)
    return coordinates


def mark_closest_coords(coordinates):
    coord_map = defaultdict(dict)

    for index in coordinates:
        coord = coordinates[index]
        coord_map[coord[0]][coord[1]] = 0

    print(coord_map)
    return coord_map


def find_min_max(coordinates):
    print("Finding min and max x/y...")

    bounds = {}

    bounds['min_x'] = coordinates[0][0]
    bounds['max_x'] = coordinates[0][0]
    bounds['min_y'] = coordinates[0][1]
    bounds['max_y'] = coordinates[0][1]

    for coord in coordinates.values():
        bounds['min_x'] = min(bounds['min_x'], coord[0])
        bounds['max_x'] = max(coord[0], bounds['max_x'])
        bounds['min_y'] = min(coord[1], bounds['min_y'])
        bounds['max_y'] = max(coord[1], bounds['max_y'])

    print(bounds)
    return bounds

def find_convex_hull(coordinates):
    convex_hull = spatial.ConvexHull(list(coordinates.values()))

    print(convex_hull.points)
    return convex_hull


def process_areas(input_file):
    print("Processing areas...")

    coordinates = load_coords(input_file)
    coord_map = mark_closest_coords(coordinates)
    bounds = find_min_max(coordinates)
    convex_hull = find_convex_hull(coordinates)



def main():
    if len(sys.argv) > 1:
        input_file = open(sys.argv[1], 'r')
        process_areas(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

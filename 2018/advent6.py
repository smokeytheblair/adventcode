import sys
from collections import defaultdict
import re
from scipy import spatial

def print_usage(name):
    print("python3 {} [-l | -d] <input_file>".format(name))
    print("-l - process the input file to find the largest non-infinite area")
    print("-d - process the input file to find the most dense area")


def load_coords(input_file):
    print("Loading coordinates...")

    coordinates = {}
    index = 0 
    for coord in input_file:
        coordinates[index] = [int(x) for x in re.findall("\d+", coord)]
        index += 1

    print("Initial points \n{}".format(coordinates))
    return coordinates


def mark_closest_coords(coordinates, bound, convex_hull):
    coord_map = {}

    for index in coordinates:
        coord = coordinates[index]
        coord_map["{}:{}".format(coord[0],coord[1])] = "{}:{}".format(index,0)

    for ring in range(1,1000):
        skipped_all_cells = True
        for index in coordinates:
            coord = coordinates[index]
            for x in range(coord[0]-ring, coord[0]+ring+1):
                for y in range(coord[1]-ring, coord[1]+ring+1):
                    # print("{} -> x:{}, y:{}".format(coord,x,y))
                    if bound['min_x'] < x  and x < bound['max_x'] and bound['min_y'] < y and y < bound['max_y']:
                        distance = abs(coord[0] - x) + abs(coord[1] - y)
                        # print("index: {}, x: {}, y: {}, distance: {}".format(index, x, y, distance))
                        if distance != ring:
                            continue
                        new_cell = "{}:{}".format(index, distance)
                        new_coord = "{}:{}".format(x,y) 
                        if coord_map.get(new_coord) != None:
                            cell = coord_map[new_coord]
                            if ":" in cell and index != int(cell.split(":")[0]):
                                old_distance = int(cell.split(":")[1])
                                if distance < old_distance:
                                    # print("## {} is overwriting {}".format(new_cell, cell)) 
                                    coord_map[x][y] = new_cell
                                    skipped_all_cells = False
                                elif distance == old_distance:
                                    coord_map[new_coord] = "."
                                    skipped_all_cells = False
                                    # print("This cell is equidistanct: distance {}, {}".format(cell, new_cell))
                        else:
                            coord_map[new_coord] = new_cell
                            skipped_all_cells = False
                            # print("cell {} distance {}, coord[{}][{}]".format(new_cell, distance, x, y))
        if skipped_all_cells:
            print("breaking out on skipped_all_cells")
            break

    print("coord_map has {} items".format(len(coord_map)))
    # print("coord_map:\n{}".format(coord_map))
    return coord_map


def find_min_max(coordinates, is_largest):
    print("Finding min and max x/y...")

    bounds = {}

    bounds['min_x'] = coordinates[1][0]
    bounds['max_x'] = coordinates[1][0]
    bounds['min_y'] = coordinates[1][1]
    bounds['max_y'] = coordinates[1][1]

    for coord in coordinates.values():
        bounds['min_x'] = min(bounds['min_x'], coord[0])
        bounds['max_x'] = max(coord[0], bounds['max_x'])
        bounds['min_y'] = min(coord[1], bounds['min_y'])
        bounds['max_y'] = max(coord[1], bounds['max_y'])

    if is_largest:
        bounds['max_y'] += int(bounds['max_x'] - bounds['min_x']/2)
        bounds['min_y'] -= int(bounds['max_x'] - bounds['min_x']/2)
        bounds['max_x'] += int(bounds['max_y'] - bounds['min_y']/2)
        bounds['min_x'] -= int(bounds['max_y'] - bounds['min_y']/2)

    print("Outer bounds \n{}".format(bounds))
    return bounds

def find_convex_hull(coordinates):
    convex_hull = spatial.ConvexHull(list(coordinates.values()))
    print("Points in the convex hull\n{}".format(convex_hull.vertices))
    print("Line segments in the convex_hull\n{}".format(convex_hull.simplices))
    return convex_hull


def find_largest_area(input_file):
    print("Processing areas...")

    coordinates = load_coords(input_file)
    bounds = find_min_max(coordinates, True)
    convex_hull = find_convex_hull(coordinates)
    coord_map = mark_closest_coords(coordinates, bounds, convex_hull)

    area_map = {}
    for index in coordinates:
        index_disqualified = False
        if index not in convex_hull.vertices:
            coords = coordinates[index];
            area_map.setdefault(index, 0);
            for key, cell in coord_map.items():
                if ":" in cell and index == int(cell.split(":")[0]):
                    area_map[index] += 1
                    x = int(key.split(":")[0])
                    y = int(key.split(":")[1])
                    if x <= bounds["min_x"] or x >= bounds["max_x"] or y <= bounds["min_y"] or y >= bounds["max_y"]:
                        index_disqualified = True;
                        area_map.pop(index, None)
                        break
            if index_disqualified:
                print("area {} disqualified as infinite.".format(index))
                continue
            print("checking point {}:{} containing {} points".format(index, coordinates[index], area_map[index]))
            # print("Area {} has these points\n{}".format(index, 
            #     [k for k,v in coord_map.items() if ":" in v and index == int(v.split(":")[0])]))
            
    max_area = max(area_map.values())
    max_index = [k for k,v in area_map.items() if v == max_area]
    
    print("Max area is {} containing {} points".format(max_index[0], max_area))

def mark_dense_area(coordinates, bounds, convex_hull):
    coord_map = {}
    for x in range(bounds["min_x"], bounds["max_x"]+1):
        for y in range(bounds["min_y"], bounds["max_y"]+1):
            # print("summing distances from {}:{} to points of origin...".format(x,y))
            coord_key = "{}:{}".format(x,y)
            coord_map.setdefault(coord_key, 0)
            for key, coord in coordinates.items():
                # print("{} is {} away from {}".format(coord_key, abs(coord[0]-x)+abs(coord[1]-y), coord))
                coord_map[coord_key] += abs(coord[0] - x) + abs(coord[1] - y)

    # print(coord_map)
    return coord_map

def find_most_dense_area(input_file):
    print("finding most dense area...")

    coordinates = load_coords(input_file)
    bounds = find_min_max(coordinates, False)
    convex_hull = find_convex_hull(coordinates)
    coord_map = mark_dense_area(coordinates, bounds, convex_hull)

    area_count = 0
    for coord, distance in coord_map.items():
        # print("coord {}, distance {}".format(coord, distance))
        if distance < 10000:
            area_count += 1

    print("size of dense area is {}".format(area_count))

def main():
    if len(sys.argv) > 2:
        input_file = open(sys.argv[2], 'r')
        if "-l" in sys.argv[1]:
            find_largest_area(input_file)
        elif "-d" in sys.argv[1]:
            find_most_dense_area(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()

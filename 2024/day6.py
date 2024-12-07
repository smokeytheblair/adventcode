import sys
import argparse

reset_report = None


def load_inputs(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        report = list(input_file)

        if reset_report is None:
            reset_report = report.copy()

    return report


def walk_the_guard(map, pos_x, pos_y, current_direction, positions_count):
    print(f"walk_the_guard starting at [{pos_x}, {pos_y}] going {current_direction}")
    history = [(pos_x, pos_y)]

    while True:
        if current_direction == "north":
            # not off the edge of the map
            if pos_y - 1 >= 0:
                if "#" == map[pos_y-1][pos_x]:
                    current_direction = "east"
                else:
                    pos_y -= 1
                    if (pos_x, pos_y) not in history:
                        positions_count += 1
                        history.append((pos_x, pos_y))
            else: # done, we've walked off the map
                break
        elif current_direction == "south":
            if pos_y + 1 < len(map):
                if "#" == map[pos_y+1][pos_x]:
                    current_direction = "west"
                else:
                    pos_y += 1
                    if (pos_x, pos_y) not in history:
                        positions_count += 1
                        history.append((pos_x, pos_y))
            else: # done, off the map
                break
        elif current_direction == "east":
            if pos_x + 1 < len(map[pos_y]):
                if "#" == map[pos_y][pos_x+1]:
                    current_direction = "south"
                else:
                    pos_x += 1
                    if (pos_x, pos_y) not in history:
                        positions_count += 1
                        history.append((pos_x, pos_y))
            else: # done, off the map
                break
        elif current_direction == "west":
            if pos_x -1 >= 0:
                if "#" == map[pos_y][pos_x-1]:
                    current_direction = "north"
                else:
                    pos_x -= 1
                    if (pos_x, pos_y) not in history:
                        positions_count += 1
                        history.append((pos_x, pos_y))
            else: # done, off the map
                break

    return positions_count


def part1(input_file):
    inputs = load_inputs(input_file)
    map = [line.strip() for line in inputs]

    positions_count = 1
    pos_x = pos_y = 0
    current_direction = "north"

    for y in range(len(map)):
        for x in range(len(map[0])):
            if '^' == map[y][x]:
                current_direction = "north"
                pos_x = x
                pos_y = y
                break
            elif '>' == map[y][x]:
                current_direction = "east"
                pos_x = x
                pos_y = y
                break
            elif '<' == map[y][x]:
                current_direction = "west"
                pos_x = x
                pos_y = y
                break
            elif 'v' == map[y][x]:
                current_direction = "south"
                pos_x = x
                pos_y = y
                break

    positions_count = walk_the_guard(map, pos_x, pos_y, current_direction, positions_count)
    print(f"Unique positions visited: {positions_count}")


def check_north(map, pos_x, pos_y):
    ret = False

    if pos_y > 0 and pos_x < len(map[0]):
        for y in range(pos_y-1, 0):
            if "#" == map[y][pos_x+1]:
                if pos_x+2 < len(map[0]):
                    for x in range(pos_x+2, len(map[0])):
                        if "#" == map[y+1][x] and "." == map[pos_y+1][x-1]:
                            ret = True
                            print(f"check_north [{pos_x}, {pos_y}] = {ret} [{x-1}, {pos_y+1}")
                            break
                break

    return ret


def check_east(map, pos_x, pos_y):
    ret = False

    if pos_x < len(map[0]) and pos_y + 1 < len(map):
        for x in range(pos_x+1, len(map[0])):
            if "#" == map[pos_y+1][x]:
                if pos_y+2 < len(map):
                    for y in range(pos_y+2, len(map)):
                        if "#" == map[y][x-1] and '.' == map[y-1][pos_x-1]:
                            ret = True
                            print(f"check_east [{pos_x}, {pos_y}] = {ret} [{pos_x-1}, {y-1}]")
                            break
                break

    return ret


def check_south(map, pos_x, pos_y):
    print(f"check_south [{pos_x}, {pos_y}]")
    ret = False

    if pos_y > 0 and pos_x > 0:
        for y in range(pos_y+1, len(map)):
            if "#" == map[y][pos_x-1]:
                if pos_x-2 > 0:
                    for x in range(pos_x-2, 0):
                        if "#" == map[y-1][x] and "." == map[pos_y-1][x+1]:
                            ret = True
                            print(f"check_north [{pos_x}, {pos_y}] = {ret} [{x+1}, {pos_y-1}")
                            break
                break

    return ret


def check_west(map, pos_x, pos_y):
    print(f"check_west [{pos_x}, {pos_y}]")
    ret = False

    if pos_x > 0 and pos_y - 1 > 0:
        for x in range(pos_x-1, 0):
            if "#" == map[pos_y-1][x]:
                if pos_y-2 < 0:
                    for y in range(pos_y-2, 0):
                        if "#" == map[y][x+1] and '.' == map[y+1][pos_x+1]:
                            ret = True
                            print(f"check_east [{pos_x}, {pos_y}] = {ret} [{pos_x+1}, {y+1}]")
                            break
                break

    return ret


def count_looping_positions(map):
    print(f"count_looping_positions")
    looping_positions = 0

    for y in range(len(map)):
        for x in range(len(map[0])):
            if "#" == map[y][x]:
                if check_north(map, x, y):
                    looping_positions += 1
                if check_east(map, x, y):
                    looping_positions += 1
                if check_west(map, x, y):
                    looping_positions += 1
                if check_south(map, x, y):
                    looping_positions += 1

    return looping_positions


def part2(input_file):
    inputs = load_inputs(input_file)
    map = [line.strip() for line in inputs]
    print(f"map: {map}")

    positions_count = count_looping_positions(map)
    print(f"Looping positions: {positions_count}")


def main():
    parser = argparse.ArgumentParser(description="Advent of Code.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='--part=1 or --part=2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                part1(input_file)
            elif args.part == 2:
                part2(input_file)


if __name__ == "__main__":
    main()


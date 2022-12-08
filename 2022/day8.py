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


def check_visibility(tree_grid, y, x):
    vis_left = vis_right = vis_up = vis_down = True

    # scan left
    for x1 in range(x-1, -1, -1):
        if tree_grid[y][x] <= tree_grid[y][x1]:
            vis_left = False
            break

    # scan right
    for x1 in range(x+1, len(tree_grid[0])):
        if tree_grid[y][x] <= tree_grid[y][x1]:
            vis_right = False
            break

    # scan up
    for y1 in range(y-1, -1, -1):
        if tree_grid[y][x] <= tree_grid[y1][x]:
            vis_up = False
            break

    # scan down
    for y1 in range(y+1, len(tree_grid)):
        if tree_grid[y][x] <= tree_grid[y1][x]:
            vis_down = False
            break

    return vis_left or vis_right or vis_up or vis_down


def count_visible_trees(tree_grid):
    # all edge trees are visible
    visible_count = (len(tree_grid) * 2) + ((len(tree_grid[0])-2) * 2)

    for y in range(len(tree_grid)):
        for x in range(len(tree_grid[0])):
            # print(f"tree[{y}][{x}]: {tree_grid[y][x]}")
            # edges are already counted above
            if 0 == x or 0 == y or x == len(tree_grid[0])-1 or y == len(tree_grid) - 1:
                continue
            else:
                if check_visibility(tree_grid, y, x):
                    visible_count += 1

    return visible_count


def count_view(tree_grid, y, x):
    vis_left = vis_right = vis_up = vis_down = 0

    # scan left
    for x1 in range(x-1, -1, -1):
        vis_left += 1

        if tree_grid[y][x] <= tree_grid[y][x1]:
            break

    # scan right
    for x1 in range(x+1, len(tree_grid[0])):
        vis_right += 1

        if tree_grid[y][x] <= tree_grid[y][x1]:
            break

    # scan up
    for y1 in range(y-1, -1, -1):
        vis_up += 1

        if tree_grid[y][x] <= tree_grid[y1][x]:
            break

    # scan down
    for y1 in range(y+1, len(tree_grid)):
        vis_down += 1

        if tree_grid[y][x] <= tree_grid[y1][x]:
            break

    print(f"tree[{y}][{x}]: {tree_grid[y][x]} => {vis_left} * {vis_right} * {vis_up} * {vis_down} = {vis_left * vis_right * vis_up * vis_down}")
    return vis_left * vis_right * vis_up * vis_down


def find_biggest_view(tree_grid):
    # all edge trees are visible
    visible_count = 0

    for y in range(len(tree_grid)):
        for x in range(len(tree_grid[0])):
            # print(f"tree[{y}][{x}]: {tree_grid[y][x]}")
            visible_count = max(visible_count, count_view(tree_grid, y, x))

    return visible_count


def part1(input_file):
    trees = load_inputs(input_file)

    tree_grid = []
    for tree_row in trees:
        tree_grid.append([int(tree) for tree in tree_row.strip()])

    print(tree_grid)

    visible_count = count_visible_trees(tree_grid)

    print(f"visible trees: {visible_count}")


def part2(input_file):
    trees = load_inputs(input_file)

    tree_grid = []
    for tree_row in trees:
        tree_grid.append([int(tree) for tree in tree_row.strip()])

    print(tree_grid)

    visible_count = find_biggest_view(tree_grid)

    print(f"biggest view: {visible_count}")


def main():
    parser = argparse.ArgumentParser(description="Advent of Code.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                part1(input_file)
            elif args.part == 2:
                part2(input_file)


if __name__ == "__main__":
    main()


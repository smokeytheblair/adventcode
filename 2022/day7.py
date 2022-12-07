import sys
import argparse
from anytree import Node, RenderTree, ContStyle, PreOrderIter, Resolver

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


def build_tree(inputs):
    dir_tree = Node('root', parent=None)
    curr_dir = dir_tree
    curr_dir_name = ''
    r = Resolver('name')

    for line in inputs:
        commands = [x.strip() for x in line.split(' ')]

        if '$' == commands[0]:
            if 'cd' == commands[1]:
                if '..' == commands[2]:
                    curr_dir = r.get(curr_dir, '..')
                elif '/' == commands[2]:
                    curr_dir = dir_tree
                    curr_dir_name = commands[2]
                else:
                    curr_dir_name = commands[2]
                    curr_path = curr_dir.path
                    curr_dir = r.get(curr_dir, curr_dir_name)
            elif 'ls' == commands[1]:
                continue
        elif 'dir' == commands[0]:
            Node(commands[1], curr_dir)
        elif commands[0].isnumeric():
            Node(line.strip(), curr_dir)

    print(f"dir_tree: {RenderTree(dir_tree, style=ContStyle())}")
    return dir_tree


def absolute_path(node):
    path = ""
    print(node)
    for dir in node:
        path = path + "/" + dir.name

    return path


def sum_directory_sizes(input_file):
    inputs = load_inputs(input_file)

    dir_tree = build_tree(inputs)

    max_dir_size = 100000
    dir_sizes = {}
    for node in PreOrderIter(dir_tree):
        dir_path = node.name
        if dir_path[0].isnumeric():
            size, name = dir_path.split()
            print(f"dir path: {absolute_path(node.parent.path)}")
            dir_sizes[absolute_path(node.parent.path)] += int(size)
            print(f"adding {size} to {node.parent.name} for size = {dir_sizes[absolute_path(node.parent.path)]}")
            parent_node = node.parent # parent of file
            parent_node = parent_node.parent #parent directory
            while parent_node is not None:
                dir_sizes[absolute_path(parent_node.path)] += int(size)
                print(f"adding {size} to {parent_node.name} for size = {dir_sizes[absolute_path(parent_node.path)]}")

                parent_node = parent_node.parent
        else:
            if node is not None:
                dir_sizes[absolute_path(node.path)] = 0


    total_size = 0
    for value in dir_sizes.values():
        if value <= max_dir_size:
            total_size += value

    print(f"dir_sizes: {dir_sizes}")
    print(f"sum of dirs: {total_size}")

def find_dir_to_delete(input_file):
    inputs = load_inputs(input_file)

    dir_tree = build_tree(inputs)

    dir_sizes = {}
    for node in PreOrderIter(dir_tree):
        dir_path = node.name
        if dir_path[0].isnumeric():
            size, name = dir_path.split()
            print(f"dir path: {absolute_path(node.parent.path)}")
            dir_sizes[absolute_path(node.parent.path)] += int(size)
            print(f"adding {size} to {node.parent.name} for size = {dir_sizes[absolute_path(node.parent.path)]}")
            parent_node = node.parent # parent of file
            parent_node = parent_node.parent #parent directory
            while parent_node is not None:
                dir_sizes[absolute_path(parent_node.path)] += int(size)
                print(f"adding {size} to {parent_node.name} for size = {dir_sizes[absolute_path(parent_node.path)]}")

                parent_node = parent_node.parent
        else:
            if node is not None:
                dir_sizes[absolute_path(node.path)] = 0

    disk_size = 70000000
    free_space = 30000000
    curr_disk_usage = disk_size - dir_sizes["/root"]
    needed_space = free_space - curr_disk_usage

    print(f"curr_disk_usage: {curr_disk_usage}, needed_space: {needed_space}")

    min_dir_size = disk_size
    target_dir = ''
    for key, size in dir_sizes.items():
        if size > needed_space:
            min_dir_size = min(size, min_dir_size)
            if min_dir_size == size:
                target_dir = key

    print(f"target dir: {target_dir}: {min_dir_size}")


def main():
    parser = argparse.ArgumentParser(description="Day 7")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                sum_directory_sizes(input_file)
            elif args.part == 2:
                find_dir_to_delete(input_file)



if __name__ == "__main__":
    main()


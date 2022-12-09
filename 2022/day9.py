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


def part1(input_file):
    inputs = load_inputs(input_file)

    coords_visited = set()
    head_point = [0, 0]
    tail_point = [0, 0]
    coords_visited.add(str(tail_point))
    for instr in inputs:
        direction, str_count = instr.strip().split(' ')
        count = int(str_count)

        x = head_point[0]
        y = head_point[1]

        if direction == 'U':
            for i in range(y, y + count):
                head_point[1] += 1

                if abs(head_point[1] - tail_point[1]) > 1 and head_point[0] != tail_point[0]:
                    tail_point[0] = head_point[0]

                if abs(head_point[1] - tail_point[1]) > 1:
                    tail_point[1] += 1

                coords_visited.add(str(tail_point))
        elif direction == 'D':
            for i in range(y, y - count, -1):
                head_point[1] -= 1

                if abs(head_point[1] - tail_point[1]) > 1 and head_point[0] != tail_point[0]:
                    tail_point[0] = head_point[0]

                if abs(head_point[1] - tail_point[1]) > 1:
                    tail_point[1] -= 1

                coords_visited.add(str(tail_point))
        elif direction == 'R':
            for i in range(x, x + count):
                head_point[0] += 1

                if head_point[1] != tail_point[1] and abs(head_point[0] - tail_point[0]) > 1:
                    tail_point[1] = head_point[1]

                if abs(head_point[0] - tail_point[0]) > 1:
                    tail_point[0] += 1

                coords_visited.add(str(tail_point))
        elif direction == 'L':
            for i in range(x, x - count, -1):
                head_point[0] -= 1

                if head_point[1] != tail_point[1] and abs(head_point[0] - tail_point[0]) > 1:
                    tail_point[1] = head_point[1]

                if abs(head_point[0] - tail_point[0]) > 1:
                    tail_point[0] -= 1

                coords_visited.add(str(tail_point))

        print(f"{direction}, {count}")

    print(f"Nodes visited: {len(coords_visited)}")


def part2(input_file):
    inputs = load_inputs(input_file)

    num_knots = 10
    coords_visited = set()

    rope = []
    for i in range(num_knots):
        rope.append([1000, 1000])

    coords_visited.add(str(rope[9]))

    for instr in inputs:
        direction, str_count = instr.strip().split(' ')
        count = int(str_count)
        print(f"{direction}, {count}")

        if direction == 'U':
            for i in range(count):
                for knot in range(num_knots):
                    if knot == 9:
                        coords_visited.add(str(rope[knot]))
                        break

                    head_point = rope[knot]
                    tail_point = rope[knot + 1]

                    if 0 == knot:
                        head_point[1] += 1

                    if abs(head_point[1] - tail_point[1]) > 1 and head_point[0] != tail_point[0] or \
                            abs(head_point[0] - tail_point[0]) > 1 and head_point[1] != tail_point[1]:
                        if head_point[0] < tail_point[0]:
                            tail_point[0] -= 1
                        else:
                            tail_point[0] += 1

                        if head_point[1] < tail_point[1]:
                            tail_point[1] -= 1
                        else:
                            tail_point[1] += 1
                    elif abs(head_point[1] - tail_point[1]) > 1:
                        tail_point[1] += 1
                    elif abs(head_point[0] - tail_point[0]) > 1:
                        if head_point[0] > tail_point[0]:
                            tail_point[0] += 1
                        else:
                            tail_point[0] -= 1
        elif direction == 'D':
            for i in range(count):
                for knot in range(num_knots):
                    if knot == 9:
                        coords_visited.add(str(rope[knot]))
                        break

                    head_point = rope[knot]
                    tail_point = rope[knot + 1]

                    if 0 == knot:
                        head_point[1] -= 1

                    if abs(head_point[1] - tail_point[1]) > 1 and head_point[0] != tail_point[0] or \
                            abs(head_point[0] - tail_point[0]) > 1 and head_point[1] != tail_point[1]:
                        if head_point[0] < tail_point[0]:
                            tail_point[0] -= 1
                        else:
                            tail_point[0] += 1

                        if head_point[1] < tail_point[1]:
                            tail_point[1] -= 1
                        else:
                            tail_point[1] += 1
                    elif abs(head_point[1] - tail_point[1]) > 1:
                        tail_point[1] -= 1
                    elif abs(head_point[0] - tail_point[0]) > 1:
                        if head_point[0] > tail_point[0]:
                            tail_point[0] += 1
                        else:
                            tail_point[0] -= 1
        elif direction == 'R':
            for i in range(count):
                for knot in range(num_knots):
                    if knot == 9:
                        coords_visited.add(str(rope[knot]))
                        break

                    head_point = rope[knot]
                    tail_point = rope[knot + 1]

                    if 0 == knot:
                        head_point[0] += 1

                    if head_point[1] != tail_point[1] and abs(head_point[0] - tail_point[0]) > 1 or \
                            head_point[0] != tail_point[0] and abs(head_point[1] - tail_point[1]) > 1:
                        if head_point[1] < tail_point[1]:
                            tail_point[1] -= 1
                        else:
                            tail_point[1] += 1

                        if head_point[0] < tail_point[0]:
                            tail_point[0] -= 1
                        else:
                            tail_point[0] += 1
                    elif abs(head_point[0] - tail_point[0]) > 1:
                        tail_point[0] += 1
                    elif abs(head_point[1] - tail_point[1]) > 1:
                        if head_point[1] > tail_point[1]:
                            tail_point[1] += 1
                        else:
                            tail_point[1] -= 1
        elif direction == 'L':
            for i in range(count):
                for knot in range(num_knots):
                    if knot == 9:
                        coords_visited.add(str(rope[knot]))
                        break

                    head_point = rope[knot]
                    tail_point = rope[knot + 1]

                    if 0 == knot:
                        head_point[0] -= 1

                    if head_point[1] != tail_point[1] and abs(head_point[0] - tail_point[0]) > 1 or \
                            head_point[0] != tail_point[0] and abs(head_point[1] - tail_point[1]) > 1:
                        if head_point[1] < tail_point[1]:
                            tail_point[1] -= 1
                        else:
                            tail_point[1] += 1

                        if head_point[0] < tail_point[0]:
                            tail_point[0] -= 1
                        else:
                            tail_point[0] += 1
                    elif abs(head_point[0] - tail_point[0]) > 1:
                        tail_point[0] -= 1
                    elif abs(head_point[1] - tail_point[1]) > 1:
                        if head_point[1] > tail_point[1]:
                            tail_point[1] += 1
                        else:
                            tail_point[1] -= 1

    print(f"Nodes visited: {len(coords_visited)}")


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


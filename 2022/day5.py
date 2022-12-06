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


def create_stacks(crates_map):
    crates = {}
    for row in crates_map:
        if 0 == len(crates):
            for num in row.split('   '):
                crates[int(num.strip())] = []
        else:
            print(f"row: {row}")
            counter = 0
            for key in crates.keys():
                offset = key+(counter*3)
                if offset < len(row):
                    crate = row[offset]
                else:
                    crate = ' '

                counter += 1
                print(f"key: {key}, crate: {crate}")
                if crate.isalnum():
                    crates[key].append(crate)

    print(f"crates: {crates}")
    return crates


def create_instructions(instructions_map):
    instructions = []

    for row in instructions_map:
        terms = row.split(' ')

        move = []
        for term in terms:
            if term.strip().isnumeric():
                move.append(int(term))

        instructions.append(move)

    print(f"Instructions: {instructions}")
    return instructions


def move_crates(crates, instructions):
    for instruction in instructions:
        count = instruction[0]
        src = instruction[1]
        dest = instruction[2]

        for i in range(count):
            crates[dest].append(crates[src].pop(len(crates[src])-1))

    return crates


def move_crates_2(crates, instructions):
    for instruction in instructions:
        count = instruction[0]
        src = instruction[1]
        dest = instruction[2]

        move_list = crates[src][-count:]

        for i in range(count):
            crates[dest].append(move_list[i])
            crates[src].pop(len(crates[src])-1)

    return crates


def find_top_crates(input_file):
    crates_and_instructions = load_inputs(input_file)

    split_index = crates_and_instructions.index('\n')

    crates_map = crates_and_instructions[:split_index]
    crates_map.reverse()
    instructions_map = crates_and_instructions[split_index+1:]

    crates = create_stacks(crates_map)
    instructions = create_instructions(instructions_map)

    crates = move_crates(crates, instructions)

    tops = ''
    for stack in crates.values():
        tops += stack[len(stack)-1]

    print(f"new crates: {crates}")
    print(f"Tops: {tops}")


def find_top_crates_2(input_file):
    crates_and_instructions = load_inputs(input_file)

    split_index = crates_and_instructions.index('\n')

    crates_map = crates_and_instructions[:split_index]
    crates_map.reverse()
    instructions_map = crates_and_instructions[split_index+1:]

    crates = create_stacks(crates_map)
    instructions = create_instructions(instructions_map)

    crates = move_crates_2(crates, instructions)

    tops = ''
    for stack in crates.values():
        tops += stack[len(stack)-1]

    print(f"new crates: {crates}")
    print(f"Tops: {tops}")

def main():
    parser = argparse.ArgumentParser(description="Day 5")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                find_top_crates(input_file)
            elif args.part == 2:
                find_top_crates_2(input_file)


if __name__ == "__main__":
    main()


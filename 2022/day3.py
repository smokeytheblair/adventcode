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


def get_item_priority(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    elif item.islower():
        return ord(item) - ord('a') + 1
    else:
        print("BAD INPUT")
        return 0


def count_compartments(input_file):
    bags = load_inputs(input_file)

    priority_sum = 0
    bag_num = 1
    for bag in bags:
        compartment1 = bag[:int(len(bag)/2)]
        compartment2 = bag[int(len(bag)/2):]
        print(f"bag {bag_num}({len(bag)}): {compartment1}({len(compartment1)}), {compartment2}({len(compartment2)})")

        duplicates = []
        for item in compartment1:
            if item in compartment2 and item not in duplicates:
                duplicates.append(item)
                priority_sum += get_item_priority(item)
                print(f"bag {bag_num}, item \'{item}\' = {get_item_priority(item)}")

        bag_num += 1

    print(f"priority_sum = {priority_sum}")


def count_compartments_2(input_file):
    bags = load_inputs(input_file)

    priority_sum = 0
    for i in range(int(len(bags)/3)):
        offset = i*3
        bag1 = bags[offset+0]
        bag2 = bags[offset+1]
        bag3 = bags[offset+2]

        bag1_len = len(bag1)
        bag2_len = len(bag2)
        bag3_len = len(bag3)
        lengths = [bag1_len, bag2_len, bag3_len]

        duplicates = []
        if bag1_len == max(lengths):
            for item in bag1:
                if item in duplicates:
                    continue

                duplicates.append(item)

                if item in bag2 and item in bag3:
                    priority_sum += get_item_priority(item)
                    print(f"item {item} = {get_item_priority(item)}")
                    break
        elif bag2_len == max(lengths):
            for item in bag2:
                if item in duplicates:
                    continue

                duplicates.append(item)

                if item in bag1 and item in bag3:
                    priority_sum += get_item_priority(item)
                    print(f"item {item} = {get_item_priority(item)}")
                    break
        elif bag3_len == max(lengths):
            for item in bag3:
                if item in duplicates:
                    continue

                duplicates.append(item)

                if item in bag1 and item in bag2:
                    priority_sum += get_item_priority(item)
                    print(f"item {item} = {get_item_priority(item)}")
                    break

        print(f"bag1:{bag1}\nbag2:{bag2}\nbag3:{bag3}")

    print(f"priority_sum = {priority_sum}")


def main():
    parser = argparse.ArgumentParser(description="Count depth increases.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                count_compartments(input_file)
            elif args.part == 2:
                count_compartments_2(input_file)


if __name__ == "__main__":
    main()


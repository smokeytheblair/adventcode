import sys
import argparse
import math

reset_report = None


class Monkey:
    def __init__(self, num:int, items:[], operator:str, operand:int, divisible_by:int, monkey1:int, monkey2:int):
        self.num:int = num
        self.items:[] = items

        self.operator = operator
        self.operand = operand
        self.divisible_by:int = divisible_by
        self.monkey1:int = monkey1
        self.monkey2:int = monkey2

        self.inspect_count = 0

    def __str__(self):
        return f"Monkey {self.num} inspected items {self.inspect_count} times."

    def inspect(self, monkeys):
        count = len(self.items)
        for i in range(count):
            old = self.items[0]
            new = 0

            temp_operand = 0
            if self.operand == 'old':
                temp_operand = old
            else:
                temp_operand = self.operand

            if self.operator == '+':
                new = old + temp_operand
            elif self.operator == '*':
                new = old * temp_operand

            new = math.floor(new/3)
            self.items[0] = new
            self.inspect_count += 1

            self.test(monkeys, new)

    def inspect2(self, monkeys):
        count = len(self.items)
        for i in range(count):
            old = self.items[0]
            new = 0

            temp_operand = 0
            if self.operand == 'old':
                temp_operand = old
            else:
                temp_operand = self.operand

            if self.operator == '+':
                new = old + temp_operand
            elif self.operator == '*':
                new = old * temp_operand

            self.items[0] = new
            self.inspect_count += 1

            self.test(monkeys, new)

    def test(self, monkeys, item_val):
        if len(self.items) > 0:
            if item_val % self.divisible_by == 0:
                monkeys[self.monkey1].items.append(item_val)
            else:
                monkeys[self.monkey2].items.append(item_val)

            self.items.remove(item_val)


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


def create_monkeys(inputs):

    monkeys = []

    monkey_num = 0
    monkey_items = []
    monkey1 = 0
    monkey2 = 0
    operator = ''
    operand = 0
    divisible_by = 0

    for line in inputs:
        if line.find('Monkey') > -1:
            monkey_num = int(line.strip()[7:-1])
        elif line.find('Starting') > -1:
            monkey_items = [int(item) for item in line.strip()[16:].split(', ')]
        elif line.find('Operation') > -1:
            operator = line[23]
            temp = line.strip()[23:]
            if temp.isnumeric():
                operand = int(temp)
            else:
                operand = temp
        elif line.find('Test:') > -1:
            divisible_by = int(line.strip()[19:])
        elif line.find('If true:') > -1:
            monkey1 = int(line.strip()[25:])
        elif line.find('If false:') > -1:
            temp = line.strip()[26:]
            monkey2 = int(temp)
        elif line == '\n':
            monkeys.append(Monkey(monkey_num, monkey_items, operator, operand, divisible_by, monkey1, monkey2))

    # last monkey in the list
    monkeys.append(Monkey(monkey_num, monkey_items, operator, operand, divisible_by, monkey1, monkey2))

    print(monkeys)
    return monkeys


def part1(input_file):
    inputs = load_inputs(input_file)

    monkeys = create_monkeys(inputs)

    for i in range(20):
        for monkey in monkeys:
            monkey.inspect(monkeys)

    for monkey in monkeys:
        print(monkey)

    inspection_counts = [monkey.inspect_count for monkey in monkeys]

    inspection_counts.sort(reverse=True)

    print(f"{inspection_counts[0]} * {inspection_counts[1]} == {inspection_counts[0] * inspection_counts[1]}")


def part2(input_file):
    inputs = load_inputs(input_file)

    monkeys = create_monkeys(inputs)

    for i in range(10000):
        for monkey in monkeys:
            monkey.inspect2(monkeys)

    for monkey in monkeys:
        print(monkey)

    inspection_counts = [monkey.inspect_count for monkey in monkeys]

    inspection_counts.sort(reverse=True)

    print(f"{inspection_counts[0]} * {inspection_counts[1]} == {inspection_counts[0] * inspection_counts[1]}")


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


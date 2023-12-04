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

    total_points = 0
    for card in inputs:
        card_id = int(card[5:card.index(':')])
        winning_nums = [int(x) for x in str(card[card.index(':')+2:card.index('|')-1]).split(' ') if x != '']
        my_nums = [int(x) for x in str(card[card.index('|')+2:]).split(' ') if x != '']

        # print(f'{card_id}, {winning_nums}, {my_nums}')

        card_points = 0
        for num in my_nums:
            if num in winning_nums:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points *= 2

        print(f'Card {card_id} gets {card_points} points.')
        total_points += card_points

    print(f'Total points = {total_points}')


def part2(input_file):
    inputs = load_inputs(input_file)

    cards = [1 for row in inputs]

    for card in inputs:
        card_id = int(card[5:card.index(':')])
        winning_nums = [int(x) for x in str(card[card.index(':')+2:card.index('|')-1]).split(' ') if x != '']
        my_nums = [int(x) for x in str(card[card.index('|')+2:]).split(' ') if x != '']

        # print(f'{card_id}, {winning_nums}, {my_nums}')

        matching_nums = 0
        for num in my_nums:
            if num in winning_nums:
                matching_nums += 1

        end_index = min(card_id+matching_nums, len(inputs))
        for sub_index in range(card_id, end_index):
            cards[sub_index] += 1 * cards[card_id-1]

        print(f'cards: {cards}')

    print(f'Total cards {sum(cards)}')


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


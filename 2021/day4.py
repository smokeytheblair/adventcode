import sys
import argparse

bingo_balls = None
bingo_cards = None

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def print_card_sel(card_num, x, y):
    print(f"bingo_cards card {card_num} [{x},{y}] = {bingo_cards[card_num][x][y]}")

def print_bingo_cards():
    index = 0
    for card in bingo_cards:
        print(f"Card {index}:")
        for row in card:
            print(row)
        index += 1

def load_inputs(input_file):
    global bingo_balls
    global bingo_cards

    lines = list(input_file)

    bingo_balls = lines[0].replace("\n", "").split(",")
    print(bingo_balls)

    bingo_cards = []
    card = []
    next_card = False
    for line in lines:
        line = line.replace("\n", "")
        if -1 < line.find(","):
            continue
        if line == "" or line == "\n":
            if 0 != len(card):
                print(f"1: {card}")
                bingo_cards.append(card)
            card = list()
            print(f"2: {card}")
        else:
            row = line.split(" ")
            print(f"line: {line}, row: {row}")
            card.append([[num, False] for num in row if num != ""])

    if 0 != len(card):
        bingo_cards.append(card)

    print_bingo_cards()

    return bingo_cards

def play_ball(ball_num):
    print(f"\nPlaying number *** {ball_num} *** ")
    for card in bingo_cards:
        for row in card:
            for num in row:
                if num[0] == ball_num:
                    num[1] = True

    #print_bingo_cards()

def card_wins(card):
    #check rows
    for row in card:
        row_wins = True
        for num in row:
            if num[1] == False:
                row_wins = False
        if True == row_wins:
           return True

    #check columns
    col_wins = [True] * len(card[0])
    for row in card:
        col_id = 0
        for num in row:
            if num[1] == False:
                col_wins[col_id] = False
            col_id += 1

    if True in col_wins:
        return True

    return False

def check_cards():
    index = 0
    for card in bingo_cards:
        if card_wins(card):
            return index
        index += 1

    return -1

def sum_unmarked_numbers(card):
    sum = 0
    for row in card:
        for num in row:
            if num[1] == False:
                sum += int(num[0])

    return sum

def remove_winning_cards():
    winning = True

    while winning:
        winner = check_cards()

        if -1 < winner:
            bingo_cards.remove(bingo_cards[winner])
        else:
            winning = False

def play_bingo(input_file):
    load_inputs(input_file)

    for num in bingo_balls:
        play_ball(num)

        winner = check_cards()

        if -1 < winner:
            print(f"Winning card {winner}")
            unmarked_sum = sum_unmarked_numbers(bingo_cards[winner])
            print(f"Answer: {unmarked_sum} * {num} = {unmarked_sum * int(num)}")
            break

def lose_bingo(input_file):
    load_inputs(input_file)

    losing_cards = set([x for x in range(len(bingo_cards))])
    print(losing_cards)

    for num in bingo_balls:
        play_ball(num)

        winner = check_cards()

        if -1 < winner and 1 == len(bingo_cards):
            print_bingo_cards()
            unmarked_sum = sum_unmarked_numbers(bingo_cards[0])
            print(f"Losing board {winner} score: {unmarked_sum} * {num} = {unmarked_sum * int(num)}")
            break

        if -1 < winner and 1 < len(bingo_cards):
            remove_winning_cards()

def main():
    parser = argparse.ArgumentParser(description="Bingo")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                play_bingo(input_file)
            elif args.part == 2:
                lose_bingo(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()


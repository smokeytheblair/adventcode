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
    print(f"Playing number {ball_num}")
    for card in bingo_cards:
        for row in card:
            for num in row:
                if num[0] == ball_num:
                    num[1] = True

    print_bingo_cards()

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

def filter_o2_numbers(codes, i):
#    print(f"filter o2 i: {i}, codes: {codes}")

    if len(codes) <= 1:
        return codes

    if i >= len(codes[0]):
        return codes

    count_0 = 0
    count_1 = 0
    o2_nums = []

    for code in codes:
        if code[i] == "0":
            count_0 += 1
        else:
            count_1 += 1

    for code in codes:
        if count_1 >= count_0 and code[i] == "1":
            o2_nums.append(code)
        elif count_0 > count_1 and code[i] == "0":
            o2_nums.append(code)

    return filter_o2_numbers(o2_nums, i+1)


def filter_co2_numbers(codes, i):
#    print(f"filter co2 i: {i}, codes: {codes}")
    if len(codes) <= 1:
        return codes

    if i >= len(codes[0]):
        return codes

    count_0 = 0
    count_1 = 0
    co2_nums = []

    for code in codes:
        if code[i] == "0":
            count_0 += 1
        else:
            count_1 += 1

#    print(f"count_0 = {count_0}, count_1 = {count_1}")
    for code in codes:
        if count_0 <= count_1 and code[i] == "0":
            co2_nums.append(code)
        elif count_1 < count_0 and code[i] == "1":
            co2_nums.append(code)

    return filter_co2_numbers(co2_nums, i+1)

def compute_o2_2(input_file):
    codes = load_inputs(input_file)

    num_bits = len(codes[0]) - 1
    count_0 = 0
    count_1 = 0
    o2_nums = []
    co2_nums = []
    i = 0
    #       print(f"i: {i}")
    for code in codes:
        #          print(f"direction[{i}] = {direction[i]}")
        if code[i] == "0":
            count_0 += 1
        else:
            count_1 += 1

    for code in codes:
        if count_0 > count_1 and code[i] == "0":
            o2_nums.append(code)
        elif count_1 >= count_0 and code[i] == "1":
            o2_nums.append(code)

    for code in codes:
        if count_0 <= count_1 and code[i] == "0":
            co2_nums.append(code)
        elif count_1 < count_0 and code[i] == "1":
            co2_nums.append(code)

    o2_nums = filter_o2_numbers(o2_nums, 1)
    co2_nums = filter_co2_numbers(co2_nums, 1)

    print(f"o2 {o2_nums}, co2 {co2_nums}")

    o2_setting = int(o2_nums[0],2)
    co2_setting = int(co2_nums[0],2)

    print(f"o2 * co2 = {o2_setting*co2_setting}")

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
                compute_o2_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()

